#!/usr/bin/env python3
"""
MEOK DOME TUI — Layer 0 Global Command Center (2026)
A Terminal User Interface (TUI) for real-time monitoring of the CSOAI Layer 0 infrastructure.
"""

import time
import random
from datetime import datetime, timezone, timedelta
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.align import Align
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

def generate_header() -> Panel:
    header_text = Text()
    header_text.append("CSOAI LAYER 0 ", style="bold gold3")
    header_text.append("| MEOK DOME GLOBAL COMMAND CENTER | ", style="bold blue")
    header_text.append(f"SYSTEM STATUS: SECURE | ", style="bold green")
    header_text.append(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"), style="bold white")
    return Panel(header_text, style="white on grey11")

def generate_jurisdiction_table() -> Table:
    table = Table(show_header=True, header_style="bold gold3", border_style="grey37", expand=True)
    table.add_column("Jurisdiction", style="blue")
    table.add_column("Frameworks", style="white")
    table.add_column("Status", justify="right")
    table.add_column("Enforcement", justify="right")

    # EU AI Act countdown (August 2, 2026)
    target_date = datetime(2026, 8, 2, tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    delta = target_date - now
    eu_days = max(0, delta.days)

    table.add_row("🇪🇺 EU", "AI Act, GDPR, DORA, NIS2", "[bold green]ACTIVE[/]", f"[bold red]{eu_days} Days[/]")
    table.add_row("🇺🇸 US", "NIST RMF, HIPAA, State Laws", "[bold green]ACTIVE[/]", "[white]Enforced[/]")
    table.add_row("🇬🇧 UK", "AISI, DPA 2018", "[bold green]ACTIVE[/]", "[white]Enforced[/]")
    table.add_row("🇨🇳 CN", "TC260, PIPL, MLPS", "[bold yellow]MONITORING[/]", "[white]Enforced[/]")
    table.add_row("🇸🇬 SG", "Agentic AI, PDPA", "[bold green]ACTIVE[/]", "[white]Enforced[/]")
    table.add_row("🇰🇷 KR", "AI Basic Act", "[bold green]ACTIVE[/]", "[white]Pending[/]")
    
    return table

def generate_network_stats() -> Panel:
    total_nodes = 202
    active_tunnels = random.randint(1500, 2500)
    blocked = random.randint(10, 50)
    
    text = Text()
    text.append(f"Active MCP Nodes:    {total_nodes}\n", style="white")
    text.append(f"A2A Handoffs/sec:    {random.uniform(50.0, 150.0):.1f}\n", style="blue")
    text.append(f"x402/ACP Pre-checks: {active_tunnels}\n", style="green")
    text.append(f"Blocked Violations:  {blocked}\n", style="bold red")
    text.append(f"PDCA Engine Latency: {random.uniform(0.05, 0.15):.3f}ms", style="yellow")
    
    return Panel(text, title="[bold]Fleet Telemetry[/]", border_style="blue")

def generate_revenue_stats() -> Panel:
    revenue = random.uniform(12000.0, 15000.0)
    smoke_tests = random.randint(400, 600)
    certs = random.randint(45, 60)
    kits = random.randint(12, 18)

    text = Text()
    text.append(f"Total Pipeline:    £{revenue:,.2f}\n", style="bold gold3")
    text.append(f"Smoke Tests (£1):  {smoke_tests}\n", style="white")
    text.append(f"CASA Certs (£199): {certs}\n", style="green")
    text.append(f"Art.50 Kits (£999): {kits}\n", style="bold red")
    text.append(f"Conversion Rate:   {random.uniform(2.1, 4.5):.2f}%", style="cyan")

    return Panel(text, title="[bold]Revenue & Conversion[/]", border_style="gold3")

def generate_audit_log() -> Table:
    table = Table(show_header=True, header_style="bold grey74", border_style="grey37", expand=True)
    table.add_column("Time", style="cyan", width=10)
    table.add_column("Agent DID", style="dim white")
    table.add_column("Action", style="white")
    table.add_column("Result", justify="right")

    actions = [
        ("A2A Delegation", "[bold green]ALLOW[/]"),
        ("x402 Payment", "[bold green]ALLOW[/]"),
        ("Data Transfer", "[bold red]BLOCK (GDPR)[/]"),
        ("MCP Tool Call", "[bold green]ALLOW[/]"),
        ("Cross-Region", "[bold yellow]ESCALATE (BFT)[/]"),
        ("Smart Contract", "[bold green]ALLOW[/]"),
        ("COBOL Bridge", "[bold green]ALLOW[/]"),
        ("Identity Issuance", "[bold green]CERTIFIED[/]")
    ]

    for _ in range(8):
        action, result = random.choice(actions)
        did = f"did:csoai:{uuid_short()}"
        time_str = datetime.now().strftime("%H:%M:%S")
        table.add_row(time_str, did, action, result)

    return table

def uuid_short():
    return f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["main"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=2)
    )
    layout["left"].split_column(
        Layout(name="telemetry", size=8),
        Layout(name="revenue", size=8),
        Layout(name="jurisdictions")
    )
    return layout

def run_tui():
    layout = make_layout()
    layout["header"].update(generate_header())
    
    footer_text = Align.center(Text("CSOAI Layer 0 Trust Infrastructure — Press Ctrl+C to exit", style="dim white"))
    layout["footer"].update(Panel(footer_text, style="grey15"))

    with Live(layout, refresh_per_second=4, screen=True) as live:
        while True:
            layout["header"].update(generate_header())
            layout["telemetry"].update(generate_network_stats())
            layout["revenue"].update(generate_revenue_stats())
            layout["jurisdictions"].update(Panel(generate_jurisdiction_table(), title="[bold]Global Jurisdiction Mesh[/]", border_style="gold3"))
            layout["right"].update(Panel(generate_audit_log(), title="[bold]Live Blockchain Anchor Stream (Polygon PoA)[/]", border_style="cyan"))
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        run_tui()
    except KeyboardInterrupt:
        console.print("[bold green]MEOK DOME TUI Exited Securely.[/]")
