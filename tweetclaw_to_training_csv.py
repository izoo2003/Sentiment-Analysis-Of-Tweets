"""Convert TweetClaw exports into this notebook's training CSV format."""

from __future__ import annotations

import argparse
import csv
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any


FIELDNAMES = ["Tweet_ID", "Topic", "Sentiment", "Tweet_Content"]
TEXT_KEYS = ("Tweet_Content", "text", "full_text", "tweet", "content", "body")
ID_KEYS = ("Tweet_ID", "tweet_id", "tweetId", "id", "post_id", "url")
LIST_KEYS = ("tweets", "results", "items", "data", "records")


def read_json_records(path: Path) -> list[dict[str, Any]]:
    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []

    if path.suffix.lower() in {".jsonl", ".ndjson"}:
        return [
            record
            for line in raw.splitlines()
            if line.strip()
            for record in [json.loads(line)]
            if isinstance(record, dict)
        ]

    parsed = json.loads(raw)
    if isinstance(parsed, list):
        return [record for record in parsed if isinstance(record, dict)]

    if isinstance(parsed, dict):
        for key in LIST_KEYS:
            value = parsed.get(key)
            if isinstance(value, list):
                return [record for record in value if isinstance(record, dict)]

    raise ValueError("JSON input must be a list or contain a tweets/results/items/data list")


def read_csv_records(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_records(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".csv":
        return read_csv_records(path)
    return read_json_records(path)


def first_text(record: dict[str, Any], keys: Iterable[str]) -> str:
    for key in keys:
        value = record.get(key)
        if value is not None:
            text = str(value).strip()
            if text:
                return text
    return ""


def convert_records(
    records: Iterable[dict[str, Any]],
    *,
    topic: str,
    sentiment: str,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen_text: set[str] = set()

    for index, record in enumerate(records, start=1):
        tweet_text = first_text(record, TEXT_KEYS)
        if not tweet_text or tweet_text in seen_text:
            continue

        seen_text.add(tweet_text)
        tweet_id = first_text(record, ID_KEYS) or str(index)
        rows.append(
            {
                "Tweet_ID": tweet_id,
                "Topic": topic,
                "Sentiment": sentiment,
                "Tweet_Content": tweet_text,
            }
        )

    return rows


def write_rows(path: Path, rows: list[dict[str, str]], *, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Pass --overwrite to replace it.")

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert TweetClaw JSON, JSONL, NDJSON, or CSV exports to the notebook CSV shape."
    )
    parser.add_argument("input", type=Path, help="TweetClaw export file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("tweetclaw_training.csv"),
        help="Destination CSV file",
    )
    parser.add_argument("--topic", default="TweetClaw", help="Topic value for every converted row")
    parser.add_argument(
        "--sentiment",
        default="Neutral",
        choices=("Positive", "Negative", "Neutral"),
        help="Notebook-compatible label to apply when exports are unlabeled",
    )
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing output file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = read_records(args.input)
    rows = convert_records(records, topic=args.topic, sentiment=args.sentiment)
    write_rows(args.output, rows, overwrite=args.overwrite)
    print(f"Wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
