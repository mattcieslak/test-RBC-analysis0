#!/usr/bin/env python

"""Run this script in the root directory of a clone of rbc-analysis-template.

This script installs RBC datasets as subdatasets in inputs/data/
"""

import argparse
import logging
from pathlib import Path

from tqdm import tqdm

RBC_STUDIES = ["CCNP", "BHRC", "NKI", "HBN", "PNC"]
QC_THRESHOLDS = ["complete-pass", "complete-artifact", "warning-fail"]
TAGS = ["1.0"]


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--qc-threshold",
        choices=QC_THRESHOLDS,
        type=str,
        help="Which qc threshold to use",
    )
    parser.add_argument(
        "--release",
        choices=TAGS,
        type=str,
        help="Which release number would you use",
    )

    parser.add_argument(
        "--bold-studies",
        nargs="*",
        type=str,
        choices=RBC_STUDIES,
        help="Which BOLD datasets should be installed",
    )
    parser.add_argument(
        "--anat-studies",
        nargs="*",
        type=str,
        choices=RBC_STUDIES,
        help="Which FreeSurfer datasets should be installed",
    )
    parser.add_argument("--quiet", action="store_true", default=False)
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    if not args.quiet:
        logging.basicConfig(level=logging.INFO)
