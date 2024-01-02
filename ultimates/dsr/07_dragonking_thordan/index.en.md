---
layout: default
title: 7. Dragonking Thordan
parent: Lv 90. DSR
grand_parent: Ultimates
nav_order: 8
has_children: false
has_toc: false
permalink: /ultimates/dsr/07_dragonking_thordan/
---

# Dragonking Thordan

There are a couple of details that we should first go over before going into
the main mechanics loop.

## Mitigations

This phase requires some mitigation planning. As a baseline, start with:

<table>
  <tr>
    <td><b>Akh Morn's Edge #1</b></td>
    <td>MT Reprisal, H1 120s, D2</td>
  </tr>
  <tr>
    <td><b>Gigaflare's Edge #1</b></td>
    <td>MT 90s, ST Reprisal, D1, D4</td>
  </tr>
  <tr>
    <td><b>Akh Morn's Edge #2</b></td>
    <td>MT Reprisal, H1 180s, D3</td>
  </tr>
  <tr>
    <td><b>Gigaflare's Edge #2</b></td>
    <td>ST Reprisal, D2</td>
  </tr>
  <tr>
    <td><b>Akh Morn's Edge #3</b></td>
    <td>MT Reprisal, H1 120s, D1, D4</td>
  </tr>
</table>

Note that the above is just a *baseline* and does not make any recommendations
on how to use the other available party mitigations, like MT 90s, ST 90s,
H2 120s (*Expedient/Holos* and *Consolation/Panhaima*), or other pieces of
mitigation like Magick Barrier or Dismantle.

Add those mitigations as appropriate to supplement the above framework.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  <p><b>Tip:</b> H2's 30s mitigations should be used when Akh Morn's Edge begins
  its cast (after the second Trinity attack) to be back up in time for
  Gigaflare's Edge.</p>
  <p>90s mitigations used when Akh Morn's Edge begins its cast will cover the
  Akh Morn's Edge <em>and</em> be back up in time for the <em>next</em> Akh
  Morn's Edge.</p>
</div>

---

## Basic Mechanics

Dragonking Thordan has two basic mechanics that are worth mentioning.

### Fire/Ice of Ascalon

All of Dragonking Thordan's major mechanics are combined with either Fire or
Ice of Ascalon, which resolves together at the beginning of the mechanic.

<table>
  <tr>
    <td width="34%">
      <p>If Dragonking Thordan's swords glow <b>red</b>, he will use <em>Fire of
      Ascalon</em>, which is a point-blank AoE.</p>
      <p>Players must be <b>outside</b> his targeting circle.</p>
    </td>
    <td width="33%"><img src="images/fire_of_ascalon_01.jpg"></td>
    <td><img src="images/fire_of_ascalon_02.jpg"></td>
  </tr>
  <tr>
    <td width="34%">
      <p>If Dragonking Thordan's swords glow <b>blue</b>, he will use <em>Ice
      of Ascalon</em>, which is a donut AoE.</p>
      <p>Players must be <b>inside</b> his targeting circle.</p>
    </td>
    <td width="33%"><img src="images/ice_of_ascalon_01.jpg"></td>
    <td><img src="images/ice_of_ascalon_02.jpg"></td>
  </tr>
</table>

### Trinity

After each mechanic has completed, Dragonking Thordan will auto-attack twice.

<table>
  <tr>
    <td width="50%"><p>Each auto-attack hits <em>three</em> players:</p>
      <ul>
        <li>The player with highest aggro will get hit with dark damage, and
        gain a stack of Dark Resistance Down.</li>
        <li>The player with the second-highest aggro will get hit with light
        damage, and gain a stack of Light Resistance Down.</li>
        <li>The <b>closest</b> player will get hit, and gain a stack of Dark
        Resistance Down, Light Resistance Down, and Physical Vulnerability Up.</li>
      </ul>
    </td>
    <td><img src="images/trinity.jpg"></td>
  </tr>
</table>

Over the course of the fight, the non-tank players will rotate in to take one
auto-attack each.

<table>
  <tr>
    <td><b>After Exaflare's Edge</b></td>
    <td>D1 → D2</td>
  </tr>
  <tr>
    <td><b>After Akh Morn's Edge</b></td>
    <td>D3 → D4</td>
  </tr>
  <tr>
    <td><b>After Gigaflare's Edge</b></td>
    <td>H1 → H2</td>
  </tr>
</table>

Because of the stacking Light/Dark Resistance Down debuffs on the tanks, the
tanks will be constantly swapping aggro throughout the fight.

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  <p><b>Tip:</b> It's easy for the tanks to lose track of who is supposed to be
  tanking the boss. To help keep track of things:</p>
  <ul>
    <li>Add text to a Provoke macro so the chat log has a record of who last
    Provoked.</li>
    <li>The tank with <b>0 or 1 stack of Dark Resistance Down</b> should be
    holding aggro.</li>
  </ul>
</div>

With all that setup, we can now go over Dragonking Thordan's major mechanics.

---

## Mechanics Loop

Dragonking Thordan will execute the following loop three times:

1. [Exaflare's Edge](#exaflares-edge)
2. [Akh Morn's Edge](#akh-morns-edge)
3. [Gigaflare's Edge](#gigaflares-edge) *(this will be replaced with*
   *[Morn Afah's Edge](#morn-afahs-edge) on the third loop.)*

### Exaflare's Edge

Have the tank with aggro point Dragonking Thordan either North or South before
the start of this mechanic.

<table>
  <tr>
    <td width="50%">
      <p><b>1.</b> Three Exaflare telegraphs will appear relative to Thordan's
      orientation.</p>
    </td>
    <td><img src="images/exaflare_01.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>2.</b> Focus on the bright dot at the center of the Exaflares. This
      will be your first dodge point.</p>
      <p>If Dragonking Thordan is facing either north or south, you can also
      use the floor markings to guide your movement.</p>
    </td>
    <td><img src="images/exaflare_02.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>3.</b> When the Exaflares resolve, dodge to where the bright dot
      was.</p>
    </td>
    <td><img src="images/exaflare_03.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>4.</b> Continue dodging the next set of Exaflare AoEs.</p>
      <p>Dodging backwards (see the diagram) will <b>always</b> be safe.</p>
      <p>As you get more experienced with the mechanic, you will notice
      Exaflare patterns where you can maintain melee uptime <em>(dodging to the
      left in this case)</em>, but this is not necessary.</p>
    </td>
    <td><img src="images/exaflare_04.jpg"></td>
  </tr>
</table>

Thordan will then auto-attack twice, which should be taken by the two tanks,
and D1, followed by D2.

The tanks should continue to face Thordan north or south, away from the party.

### Akh Morn's Edge

Thordan will spawn three towers relative to where he is facing:

- One red tower at his front-left
- One red tower front-right
- One blue tower at his rear

The blue tower deals increased damage, and is meant to be taken by the tanks.

All players must be **inside** Thordan's hitbox in order to be within healing
range of both healers- remember to step inside if Thordan's swords were
originally red.

*Akh Morn's Edge* will be resolved with a 3-3-2 split.

<table>
  <tr>
    <td width="50%">
      <ul>
        <li><b>Front-left:</b> H1, D1, D3</li>
        <li><b>Front-right:</b> H2, D2, D4</li>
        <li><b>Back:</b> MT, ST</li>
      </ul>
    </td>
    <td><img src="images/akh_morn.jpg"></td>
  </tr>
</table>

Thordan will then auto-attack twice, which should be taken by the two tanks,
and D3, followed by D4.

Where Thordan faces after *Akh Morn's Edge* doesn't matter.

### Gigaflare's Edge

<table>
  <tr>
    <td width="50%">
      <p><em>Gigaflare's Edge</em> is a series of three raid-wide AoEs, each
      with an epicenter in a triangle going clockwise or anti-clockwise around
      Dragonking Thordan.</p>
      <p>This is <em>not</em> falloff damage- standing inside the marked region
      <em>(illustrating a South Gigaflare)</em> will one-shot a player, while
      standing outside just deals heavy damage.</p>
      <p>Mitigations for <em>Gigaflare's Edge</em> should be timed as the
      entire sequence lasts 8 seconds, while several debuffs (Reprisal, Feint,
      Addle) lasts only 10 seconds.</p>
    </td>
    <td><img src="images/gigaflare.jpg"></td>
  </tr>
</table>

Thordan will then auto-attack twice, which should be taken by the two tanks,
and H1, followed by H2.

After *Gigaflare's Edge*, whoever's tanking the boss should face the boss
**directly North or South** to prepare for *Exaflare's Edge*.

The loop then repeats from *Exaflare's Edge*.

---

## Morn Afah's Edge

Dragonking Thordan will put three towers and will continually hit them in quick
order.

As each set of towers kills three players, the party can only take two rounds
of towers as there aren't enough players to take the third set.

A general kill order should resemble:

<table>
  <tr>
    <td><b>First set of towers</b></td>
    <td>H1, H2, ST</td>
  </tr>
  <tr>
    <td><b>Second set of towers</b></td>
    <td>D3, D4, MT</td>
  </tr>
  <tr>
    <td><b>Third set of towers</b></td>
    <td>Ignore <em>(let the tower failed animation wipe the party instead of
    having D1 and D2 killed by the towers.)</em></td>
  </tr>
</table>

Morn Afah's Edge towers will match the Akh Morn's Edge tower groups.

---

## Buff windows

Assuming the party used potions at the start of P6, the buff/pot window timings
are:

<table>
  <tr>
    <td><b>First buff window + potions</b></td>
    <td>After Gigaflare's Edge #1</td>
  </tr>
  <tr>
    <td><b>Second buff window</b></td>
    <td>During Akh Morn's Edge #3</td>
  </tr>
</table>

---

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Mitigation]</b> Why doesn't the mit plan contain <em>all</em> the basic
  party mitigations for the phase? Why are MT90s, ST90s and H2 120s missing?</p>
</summary>
<table>
  <tr>
    <td>
      <p>This is partly a spillover effect from <em>Alternative End</em>,
      because depending on whether the party has a SCH or a SGE, the H2 may or
      may not have their 120s mitigation (<em>Expedient</em> versus
      <em>Holos</em>) available.</p>
      <p>SCH and SGE also have different preferences when it comes to their
      shielding 120s (<em>Consolation</em> versus <em>Panhaima</em>)- in
      particular, SGE would want to use <em>Panhaima</em> to mitigate <em>Akh
      Morn's Edge</em>, while the ability to <em>Summon Seraph</em> well in
      advance of applying <em>Consolation</em> makes it well suited for
      <em>Gigaflare's Edge</em>.</p>
      <p>Notionally, I also don't have a good way to separate the "shield" H2
      120s (<em>Consolation</em> versus <em>Panhaima</em>) from the
      "mitigation" H2 120s (<em>Expedient</em> versus <em>Holos</em>) which
      would add to the confusion. As a result, I would prefer to just leave it
      up to the player to determine how to best supplement the provided
      framework.</p>
      <p>There are also differences with the tank mitigations- the "shield" 90s
      mitigations (<em>Shake It Off</em> versus <em>Divine Veil</em>) are
      particularly nice at <em>Gigaflare's Edge</em> (also for their added
      bonus heal), while the "mitigation" 90s (<em>Dark Missionary</em> and
      <em>Heart of Light</em>) shine against <em>Akh Morn's Edge</em>.</p>
      <p>The 90s cooldown also means that timed correctly, you can get a third
      use out of the tank mitigations for the second and third <em>Akh Morn's
      Edge</em>.</p>
      <p>There's also the fine print on <em>Shake It Off</em> which would
      dispel a WAR's mitigations if used in the wrong order. Since
      <em>Vengeance</em> use isn't specified, nor whether the WAR would be MT
      or ST, it is left to the player to determine when best to use <em>Shake
      It Off</em>.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Mitigation]</b> Is there a reason D2 is paired with D4? What happens with
  double caster parties? Wouldn't that overlap Addles?</p>
</summary>
<table>
  <tr>
    <td><p>Pairing D1 with D4 is something I considered, but decided against
    as "D2 Feint first" breaks the usual pattern of D1 > D2.</p>
    <p>That being said, the important part of the mitigation plan is
    establishing the baseline for where D4 uses their Addle. That way, the
    second caster knows where not to Addle (regardless of whether they're D2 or
    D1).</p>
    <p>The same reasoning applies to double-ranged parties.</p>
    </td>
  </tr>
</table>
</details>

---

## Troubleshooting

<details markdown=block>
<summary>
  <b>[Akh Morn's Edge]</b> How did my WAR die?</p>
</summary>
<table>
  <tr>
    <td>
      <p>Check that the WAR did not use <em>Shake It Off</em> after
      <em>Vengeance</em>, as <em>Shake It Off</em> removes a WAR's buffs
      (except for <em>Rampart</em>) if used later.</p>
      <p>This is something to pay attention to in the second <em>Akh Morn's
      Edge</em> in particular, as <em>Shake It Off</em> comes back off
      cooldown there after using it at <em>Alternative End</em>.</p>
    </td>
  </tr>
</table>
</details>