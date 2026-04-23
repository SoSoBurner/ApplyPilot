"""Smoke tests: package imports and CLI invokes without error."""
from __future__ import annotations

import importlib

from typer.testing import CliRunner


def test_package_imports():
    importlib.import_module("applypilot")
    importlib.import_module("applypilot.cli")
    importlib.import_module("applypilot.pipeline")
    importlib.import_module("applypilot.config")
    importlib.import_module("applypilot.database")
    importlib.import_module("applypilot.llm")
    importlib.import_module("applypilot.view")


def test_subpackages_import():
    # applypilot.discovery.jobspy imports `jobspy`, which the README documents
    # as an optional runtime dep installed separately with --no-deps. Skip it
    # here so the smoke test stays green without that side-channel install.
    for mod in (
        "applypilot.apply.chrome",
        "applypilot.apply.dashboard",
        "applypilot.apply.launcher",
        "applypilot.apply.prompt",
        "applypilot.discovery.smartextract",
        "applypilot.discovery.workday",
        "applypilot.enrichment.detail",
        "applypilot.scoring.scorer",
        "applypilot.scoring.tailor",
        "applypilot.scoring.cover_letter",
        "applypilot.scoring.validator",
        "applypilot.scoring.pdf",
        "applypilot.wizard.init",
    ):
        importlib.import_module(mod)


def test_cli_help():
    from applypilot.cli import app

    result = CliRunner().invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "applypilot" in result.stdout.lower() or "usage" in result.stdout.lower()
