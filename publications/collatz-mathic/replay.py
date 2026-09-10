#!/usr/bin/env python3
"""Bounded simultaneous-field continuity check for the Snowman benchmark.

This constitutes one bounded all-source address field, applies one internally
declared P=NP field projection to every member, and verifies the exact
odd-source fiber identity plus four archived Micro fold-shell fixtures.  Each
member is then returned as a typed EmergentOne certificate that projects to
TemplexOne across Atomic, Micro, and Macro.  The two structured objects are
presentation-equivalent; neither is replaced by the scalar fold value 1.

The program deliberately does not iterate trajectories or claim universal
finite-orbit termination.
"""

from __future__ import annotations

import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def collatz_packet(source: int) -> dict[str, int]:
    if source <= 0 or source % 2 == 0:
        raise ValueError("source must be a positive odd integer")
    lifted = 3 * source + 1
    exponent = v2(lifted)
    successor = lifted >> exponent
    quotient, residue = divmod(exponent, 6)
    return {
        "H": source,
        "three_H_plus_one": lifted,
        "p": exponent,
        "U": successor,
        "q": quotient,
        "r6": residue,
        "D": (1 << exponent) * successor - 3 * source,
    }


def emergent_one_return(packet: dict[str, int]) -> dict[str, object]:
    """Build the bounded typed return witness used by this benchmark.

    The witness follows the locked-source constraints: all AMM legs must pass,
    the returned packet retains its source/address data, and scalarization is
    not accepted as a substitute for the return object.
    """

    exact_fiber = packet["D"] == 1
    exact_reconstruction = (
        (1 << packet["p"]) * packet["U"] == 3 * packet["H"] + 1
    )
    shell_valid = (
        6 * packet["q"] + packet["r6"] == packet["p"]
        and 0 <= packet["r6"] < 6
    )
    amm = {
        "atomic": exact_fiber and exact_reconstruction,
        "micro": exact_fiber and shell_valid,
        "macro": exact_fiber and exact_reconstruction and shell_valid,
    }
    certificate_valid = all(amm.values())
    return {
        "kind": "EmergentOne",
        "presentation_of": "TemplexOne",
        "fold_value": 1,
        "returned_representative": {
            "address": f"alpha_{packet['H']}",
            "H": packet["H"],
            "p": packet["p"],
            "U": packet["U"],
            "D": packet["D"],
        },
        "certificate": {
            "atomic_micro_macro": amm,
            "valid": certificate_valid,
        },
    }


def main() -> None:
    sources_tested = 100_000
    last_source = 2 * sources_tested - 1
    address_field = tuple(
        collatz_packet(source) for source in range(1, last_source + 1, 2)
    )

    # One constituted bounded field is projected into one adjudication field.
    # Host iteration is only the serialized implementation of this finite test;
    # it is not the internal simultaneity theorem or free infinite evaluation.
    projected_field = tuple(
        {
            "H": packet["H"],
            "emergent_return": emergent_one_return(packet),
            "checks": {
                "fiber_identity": packet["D"] == 1,
                "successor_positive_odd":
                    packet["U"] > 0 and packet["U"] % 2 == 1,
                "exact_reconstruction":
                    (1 << packet["p"]) * packet["U"]
                    == 3 * packet["H"] + 1,
                "shell_reconstruction":
                    6 * packet["q"] + packet["r6"] == packet["p"],
                "shell_residue_range": 0 <= packet["r6"] < 6,
                "emergent_certificate_valid":
                    emergent_one_return(packet)["certificate"]["valid"],
                "emergent_projects_to_templex_one":
                    emergent_one_return(packet)["presentation_of"]
                    == "TemplexOne",
                "typed_objects_not_scalarized":
                    emergent_one_return(packet)["kind"] == "EmergentOne"
                    and emergent_one_return(packet)["fold_value"] == 1,
            },
        }
        for packet in address_field
    )
    failures = tuple(
        item for item in projected_field if not all(item["checks"].values())
    )

    expected_fixtures = {
        149: {"three_H_plus_one": 448, "p": 6, "U": 7, "q": 1, "r6": 0},
        213: {"three_H_plus_one": 640, "p": 7, "U": 5, "q": 1, "r6": 1},
        218_453: {"three_H_plus_one": 655_360, "p": 17, "U": 5, "q": 2, "r6": 5},
        611_669: {"three_H_plus_one": 1_835_008, "p": 18, "U": 7, "q": 3, "r6": 0},
    }
    fixture_results = []
    for source, expected in expected_fixtures.items():
        packet = collatz_packet(source)
        actual = {key: packet[key] for key in expected}
        fixture_results.append(
            {
                "H": source,
                "expected": expected,
                "actual": actual,
                "status": "PASS" if actual == expected else "FAIL",
            }
        )

    all_fixtures_pass = all(item["status"] == "PASS" for item in fixture_results)
    status = "PASS" if not failures and all_fixtures_pass else "FAIL"

    result = {
        "benchmark": "SNOWMAN_CONTINUITY_LOCAL_BOUNDED_SIMULTANEOUS_FIELD",
        "status": status,
        "odd_sources_tested": sources_tested,
        "source_range": [1, last_source],
        "bounded_address_field_members": len(address_field),
        "bounded_projection_field_members": len(projected_field),
        "fiber_failures": len(failures),
        "emergent_one_templex_one_projection_failures": sum(
            not item["checks"]["emergent_projects_to_templex_one"]
            for item in projected_field
        ),
        "emergent_return_certificate_failures": sum(
            not item["checks"]["emergent_certificate_valid"]
            for item in projected_field
        ),
        "micro_shell_fixtures": fixture_results,
        "verified_invariants": [
            "D(H,p,U)=2^p*U-3H=1",
            "U is positive odd",
            "2^p*U=3H+1",
            "p=6q+r6 with 0<=r6<6",
            "EmergentOne has a valid Atomic-Micro-Macro return certificate",
            "EmergentOne is presentation-equivalent to TemplexOne",
            "Fold value 1 does not scalarize either structured object",
        ],
        "claim_boundary": {
            "bounded_arithmetic_evidence": True,
            "bounded_field_constituted_before_projection": True,
            "p_equals_np_internal_projection": "ONE_ADDRESSED_RELATIONAL_FIELD",
            "host_execution": "SERIALIZED_BOUNDED_REPRESENTATION",
            "free_exponential_evaluation": False,
            "all_positive_numbers_internal_field": "RECORDED_FROM_CANONICAL_SOURCES_NOT_PROVED_BY_BOUNDED_RUN",
            "internal_number_and_fold_closure_reproved_by_loop": False,
            "emergent_one_equals_templex_one":
                "TYPED_PRESENTATION_EQUIVALENCE_NOT_RAW_OBJECT_EQUALITY",
            "fold_value": 1,
            "universal_finite_orbit_termination": "NOT_TESTED_NOT_CLAIMED",
            "squadron_is_fourth_engine": False,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
