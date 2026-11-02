"""__main__.py — Run all OSCA simulation scenarios."""

from simulation.runner import print_summary, run_all
from simulation.scenarios.happy_path import scenario as happy_path
from simulation.scenarios.scope_escalation import scenario as scope_escalation
from simulation.scenarios.tier_collusion import scenario as tier_collusion
from simulation.attacks.replay_attack import scenario as replay_attack
from simulation.attacks.tamper_attack import scenario as tamper_attack


def main() -> None:
    scenarios = {
        "happy_path": happy_path,
        "scope_escalation": scope_escalation,
        "tier_collusion": tier_collusion,
        "replay_attack": replay_attack,
        "tamper_attack": tamper_attack,
    }
    results = run_all(scenarios)
    print_summary(results)


if __name__ == "__main__":
    main()
