import Mathlib

namespace TRYX.NS

theorem one_tension_accounting (g c d : ℝ) :
    g + max (-(g - c - d)) 0 = c + d + max (g - c - d) 0 := by
  rcases le_total 0 (g - c - d) with h | h
  · rw [max_eq_left h, max_eq_right (neg_nonpos.mpr h)]
    ring
  · rw [max_eq_right h, max_eq_left (neg_nonneg.mpr h)]
    ring

theorem v6_recorded_positive_remainder  :
    max ((82087564089412 : ℝ) / 100000000000 - 13487564089412 / 100000000000 - 588) 0 = 98 := by
  norm_num

theorem v6_atomic_remainder_not_exhausted  :
    max ((82087564089412 : ℝ) / 100000000000 - 13487564089412 / 100000000000 - 588) 0 ≠ 0 := by
  norm_num

end TRYX.NS

#print axioms TRYX.NS.one_tension_accounting
#print axioms TRYX.NS.v6_recorded_positive_remainder
#print axioms TRYX.NS.v6_atomic_remainder_not_exhausted

namespace TRYX.PNP

/-- Semantic assignment carrier only; no constant-cost implementation assumption. -/
def Assignment : Nat → Type
  | 0 => Unit
  | n + 1 => Bool × Assignment n

/-- Exact current-state existential hinge. -/
def hinge {α : Type} (f : Bool × α → Bool) (a : α) : Bool :=
  f (false, a) || f (true, a)

/-- Repeated semantic elimination. Representation costs are not bounded here. -/
def resolve : (n : Nat) → (Assignment n → Bool) → Bool
  | 0, f => f ()
  | n + 1, f => resolve n (hinge f)

theorem boolean_fold_algebra (a b : Bool) :
    (if a || b then (1 : ℤ) else 0) = (if a then 1 else 0) + (if b then 1 else 0) - (if a then 1 else 0) * (if b then 1 else 0) := by
  cases a <;> cases b <;> norm_num

theorem hinge_exact {α : Type} (f : Bool × α → Bool) (a : α) :
    hinge f a = true ↔ ∃ b : Bool, f (b, a) = true := by
  constructor
  · intro h
    have h' : f (false, a) = true ∨ f (true, a) = true := by
      simpa [hinge] using h
    rcases h' with hf | ht
    · exact ⟨false, hf⟩
    · exact ⟨true, ht⟩
  · rintro ⟨b, hb⟩
    cases b <;> simp [hinge, hb]

theorem resolve_correct (n : Nat) (f : Assignment n → Bool) :
    resolve n f = true ↔ ∃ a : Assignment n, f a = true := by
  induction n with
  | zero =>
    constructor
    · intro h
      exact ⟨(), h⟩
    · rintro ⟨a, ha⟩
      cases a
      exact ha
  | succ n ih =>
    rw [resolve, ih]
    constructor
    · rintro ⟨a, ha⟩
      obtain ⟨b, hb⟩ := (hinge_exact f a).mp ha
      exact ⟨(b, a), hb⟩
    · rintro ⟨⟨b, a⟩, ha⟩
      exact ⟨a, (hinge_exact f a).mpr ⟨b, ha⟩⟩

end TRYX.PNP

#print axioms TRYX.PNP.boolean_fold_algebra
#print axioms TRYX.PNP.hinge_exact
#print axioms TRYX.PNP.resolve_correct

namespace TRYX.Snowman

/-- A retained source packet, not a bare scalar return or an orbit certificate. -/
structure Packet where
  source : Nat
  power : Nat
  oddCarrier : Nat
  sourcePositive : 0 < source
  sourceOdd : source % 2 = 1
  carrierPositive : 0 < oddCarrier
  carrierOdd : oddCarrier % 2 = 1
  reconstruction : 2 ^ power * oddCarrier = 3 * source + 1

def foldValue (q : Packet) : Nat :=
  2 ^ q.power * q.oddCarrier - 3 * q.source

theorem positive_dyadic_factorization (m : Nat) (hm : 0 < m) :
    ∃ p u : Nat, 0 < u ∧ u % 2 = 1 ∧ 2 ^ p * u = m := by
  induction m using Nat.strong_induction_on with
  | h m ih =>
    by_cases he : m % 2 = 0
    · have hp : 0 < m / 2 := by omega
      have hl : m / 2 < m := by omega
      obtain ⟨p, u, hu, ho, hr⟩ := ih (m / 2) hl hp
      refine ⟨p + 1, u, hu, ho, ?_⟩
      calc
        2 ^ (p + 1) * u = 2 * (2 ^ p * u) := by rw [pow_succ]; ring
        _ = 2 * (m / 2) := by rw [hr]
        _ = m := by omega
    · refine ⟨0, m, hm, ?_, ?_⟩
      · omega
      · simp

theorem packet_fold_one (q : Packet) :
    foldValue q = 1 := by
  unfold foldValue
  rw [q.reconstruction]
  omega

theorem all_odd_addresses_have_fold_one (h : Nat) (hpos : 0 < h) (hodd : h % 2 = 1) :
    ∃ q : Packet, q.source = h ∧ foldValue q = 1 := by
  obtain ⟨p, u, hu, ho, hr⟩ := positive_dyadic_factorization (3 * h + 1) (by omega)
  let q : Packet := ⟨h, p, u, hpos, hodd, hu, ho, hr⟩
  exact ⟨q, rfl, packet_fold_one q⟩

theorem different_sources_keep_distinct_packets (p q : Packet) (h : p.source ≠ q.source) :
    p ≠ q := by
  intro heq
  exact h (congrArg Packet.source heq)

theorem archived_four_reconstructions  :
    ((2 : Nat)^6 * 7 = 3*149+1) ∧ ((2 : Nat)^7 * 5 = 3*213+1) ∧ ((2 : Nat)^17 * 5 = 3*218453+1) ∧ ((2 : Nat)^18 * 7 = 3*611669+1) := by
  norm_num

end TRYX.Snowman

#print axioms TRYX.Snowman.positive_dyadic_factorization
#print axioms TRYX.Snowman.packet_fold_one
#print axioms TRYX.Snowman.all_odd_addresses_have_fold_one
#print axioms TRYX.Snowman.different_sources_keep_distinct_packets
#print axioms TRYX.Snowman.archived_four_reconstructions
