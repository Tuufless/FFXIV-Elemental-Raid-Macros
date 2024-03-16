---
layout: default
title: A. Mitigation
parent: Lv 90. TOP
nav_order: 9
has_children: false
has_toc: false
grand_parent: Ultimates
permalink: /ultimates/top/mitigation/
---

# Mitigation

The following is a mitigation framework for the encounter.

It is *not* a plan for every single cooldown available to the party; instead,
think of the following as a bare-bones framework to work with- i.e: these are
the things that people will generally look for when mitigation is missing.

<table>
  <th width="50%">Mitigation by Phase</th>
  <th colspan=2>Mitigation by Role</th>
  <tr>
    <td>
      <ul>
        <li><a href="#p1-omega">P1. Omega</a></li>
        <li><a href="#p2-omega-mf">P2. Omega-M/F</a></li>
        <li><a href="#p3-omega-reconfigured">P3. Omega Reconfigured</a></li>
        <li><a href="#p4-blue-screen">P4. Blue Screen</a></li>
        <li><a href="#p5-run-dynamis">P5. Run Dynamis</a></li>
        <li><a href="#p6-alpha-omega">P6. Alpha Omega</a></li>
      </ul>
    </td>
    <td>
      <ul>
        <li><a href="#mt">MT</a></li>
        <li><a href="#st">ST</a></li>
        <li><a href="#h1">H1</a></li>
        <li><a href="#h2">H2</a></li>
      </ul>
    </td>
    <td>
      <ul>
        <li><a href="#d1">D1</a></li>
        <li><a href="#d2">D2</a></li>
        <li><a href="#d3">D3</a></li>
        <li><a href="#d4">D4</a></li>
      </ul>
    </td>
  </tr>
</table>

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
<details markdown=block>
<summary>
  <b>[Click to Expand] Mitigation Notation</b>
</summary>
<table>
  <tr>
    <td>Tank 30%</td>
    <td>Vengeance, Sentinel, Shadow Wall, Nebula</td>
  </tr>
  <tr>
    <td>Tank 3rd</td>
    <td>Thrill of Battle, Bulwark, Oblation, Camouflage</td>
  </tr>
  <tr>
    <td>Tank 90s</td>
    <td>Shake It Off, Dark Missionary, Heart of Light, Divine Veil</td>
  </tr>
  <tr>
    <td>H1 120s</td>
    <td>Temperance, Neutral Sect</td>
  </tr>
  <tr>
    <td>H1 180s</td>
    <td>Liturgy of the Bell, Macrocosmos</td>
  </tr>
  <tr>
    <td>H2 30s</td>
    <td>Sacred Soil, Kerachole</td>
  </tr>
  <tr>
    <td>H2 90s</td>
    <td>Deployment Tactics, Zoe</td>
  </tr>
  <tr>
    <td>H2 120s</td>
    <td>Expedient, Holos</td>
  </tr>
  <tr>
    <td>Extra</td>
    <td>
      <p>Anything that cannot be reliably present in a party.</p>
      <ul>
        <li>Passage of Arms, Fey Illumination, Collective Unconsciousness,
        Consolation, Panhaima, Dismantle, Improvisation, Magick Barrier</li>
      </ul>
    </td>
  </tr>
</table>
</details>
</div>

## Mitigation by Phase

<div style="background-color: #002 ; padding: 10px; border: 1px solid;">
  The raw damage values have also been provided, separated into damage dealt
  to:
  <ul>
    <li><b>T</b>anks (MT, ST)</li>
    <li><b>P</b>hysical DPS (D1, D2, D3)</li>
    <li><b>M</b>agic (H1, H2, D4)</li>
  </ul>
</div>

Physical DPS jobs have higher max HP, but lower magic defense compared to
casters.

- Tanks have 110k max HP.
- Physical DPS jobs have 77k max HP.
- Magical jobs have 68k max HP.
- Basic shields *(Succor, Eukrasian Prognosis)* absorb 8k damage.

### P1. Omega

Party mitigation should be used anytime by the second Condensed Wave during 
Pantokrator. There are 6 seconds between each wave, so all tank and healer
mitigations can cover at least three waves each.

They will be comfortably back in time for their next use in P2.

<table>
  <tr>
    <td>
      <p>Condensed Wave #1</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Condensed Wave #2</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by MT Reprisal.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Condensed Wave #3</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Condensed Wave #4</p>
      <ul>
        <li><b>P:</b> 50k-67k</li>
        <li><b>M:</b> 46k-63k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by ST Reprisal.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Pantokrator (Diffuse Wave Cannon Kyrios)</p>
    </td>
    <td>
      <ul>
        <li><b>MT + ST:</b> Invuln</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>

### P2. Omega-M/F

Healer 120s mitigations will be needed to mitigate Pile Pitch + Meteors.
However, the problem is that we also need them to be available for the second
set of towers in P3- if the party does not hold DPS in P2, there is a chance
that the healer 120s won't come off cooldown in time.

- One option is to use the healer 120s to mitigate Optimized Bladedance (the 
  tethers) and Meteors.
  - The healer 120s will be back up comfortably in time for the 2nd set of
    towers in P3.
  - Lets the tanks survive Optimized Bladedance without *Rampart*, in the event
    they did not pop it early at the at the start of the phase.
  - The healer 120s will *not* cover *Cosmo Memory*.
- Alternatively, the earliest you can use the healer 120s and still cover
  *Cosmo Memory* is when the Flare markers appear.

Targeted mitigations, like *Addle*, *Feint*, and *Reprisal* have minimal use in 
this phase as the hard-hitting raid-wide damage comes from non-targetable
sources. As such, debuffs are better used on Omega-M/F's autoattacks.

<table>
  <tr>
    <td>
      <p>Solar Ray</p>
      <ul>
        <li><b>T:</b> 170-198k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Rampart, short</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Use Rampart when Omega becomes untargetable in the previous phase.</li>
        <li>A DRK should also Dark Mind.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Optimized Bladedance</p>
      <ul>
        <li><b>T:</b> 182k-231k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Rampart, 30%, 3rd, short</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Dark Mind will not work, as this is physical damage.</li>
        <li>Healer 120s can be used to help the tanks mitigate in the
        event they don't have <em>Rampart</em>, and guarantee that they will
        be available for 2nd towers in P3, but they will not cover <em>Cosmo 
        Memory</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Pile Pitch + Meteors</td>
    <td>
      <ul>
        <li>MT 90s, ST 90s, H1 120s, H2 120s, H2 30s, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The earliest you can use the healer 120s and still catch
        <em>Cosmo Memory</em> is when the Flare markers appear.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      <p>Cosmo Memory</p>
      <ul>
        <li><b>P:</b> 85k-104k</li>
        <li><b>M:</b> 76k-96k</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <ul>
        <li>This is also covered by H2 30s and D3 from Pile Pitch + Meteors,
        and possibly the healer 120s depending on when they were used.</li>
        <li>Any "extra" mitigations <em>(Magick Barrier, Passage of Arms, etc.)</em> should be used here.</li>
      </ul>
    </td>
  </tr>
</table>

### P3. Omega Reconfigured

- The party needs at least three pieces of 10% mitigation (shields count) to
  survive each round of towers and tethers *without* any healing in between.
- You can get 3-4 uses of H2 30s mitigations, depending on whether you use an
  H2 30s mitigation early at *Hello, World*.
- Tanks should mitigate Omega's autoattacks between each set of towers. Some
  groups may opt to tank swap after the second tower to cycle through both
  tank's cooldowns.

<table>
  <tr>
    <td>
      <p>Hello, World</p>
      <ul>
        <li><b>P:</b> 74k-82k</li>
        <li><b>M:</b> 68k-76k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, D1, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Towers #1</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A WAR/PLD can use <em>Shake It Off/Divine Veil</em> early here to
        get an extra use at <em>Critical Error</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Towers #2</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H1 120s, H2 120s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>This is the latest you can use healer 120s for them to be back in
        time for P4.</li>
        <li>Depending on when the healer 120s were using in P2, and the P2
        killtime, they may not be up in time to catch the full sequence, in 
        which case healers may need to heal in between tethers.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Towers #3</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Towers #4</p>
      <ul>
        <li><b>P:</b> 89k-98k</li>
        <li><b>M:</b> 74k-93k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Critical Error</p>
      <ul>
        <li><b>P:</b> 88k-97k</li>
        <li><b>M:</b> 81k-90k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>D1, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><em>Critical Error</em> needs an additional H2 30s, <em>or</em> H2
        90s to guarantee survival.</li>
        <li>Any "extra" mitigations <em>(Magick Barrier, Passage of Arms, 
        etc.)</em> should be used here.</li>
      </ul>
    </td>
  </tr>
</table>

### P4. Blue Screen

- Because the Tank 90s, D1, and D3 mitigations are being saved for *Run
  Dynamis (Delta Version)*, they *cannot* be used in this phase.
- Only the healers and D4 will be mitigating this phase (with some support
  from *Reprisal*). Where they are used does not particularly matter, so they
  have *not* been included below.
  - Each healer 120s will last two stacks and two spreads.
  - Tanks will use *Reprisal* on the first two sets of Wave Cannons.

<table>
  <tr>
    <td>
      <p>Wave Cannon #1 (spread)</p>
      <ul>
        <li><b>P:</b> 29k-41k</li>
        <li><b>M:</b> 27k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #1 (stack)</p>
      <ul>
        <li><b>P:</b> 46k-58k</li>
        <li><b>M:</b> 42k-55k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by the MT Reprisal.</li>
        <li>A SCH's <em>Expedient</em> is particularly useful here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (spread)</p>
      <ul>
        <li><b>P:</b> 29k-41k</li>
        <li><b>M:</b> 27k-37k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>ST Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (stack)</p>
      <ul>
        <li><b>P:</b> 46k-58k</li>
        <li><b>M:</b> 42k-55k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Covered by the ST Reprisal.</li>
        <li>This is the latest you can use H2 30s mitigations and have them
        back by <em>Blue Screen</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #3 (spread)</p>
      <ul>
        <li><b>P:</b> 29k-41k</li>
        <li><b>M:</b> 27k-37k</li>
      </ul>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #3 (stack)</p>
      <ul>
        <li><b>P:</b> 46k-58k</li>
        <li><b>M:</b> 42k-55k</li>
      </ul>
    </td>
    <td></td>
    <td>
      <ul>
        <li>Healer 120s mitigations used here will also cover <em>Blue
        Screen</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Blue Screen</p>
      <ul>
        <li><b>P:</b> 71k-81k</li>
        <li><b>M:</b> 69k-76k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 30s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 120s can be used to substitute for shields or H2 30s.</li>
      </ul>
    </td>
  </tr>
</table>

### P5. Run Dynamis

There are a number of details when it comes to mitigating this phase:

- How the party handles *Solar Ray* will largely depend on whether a WAR is in
  the party.
  - If you have a WAR, then both tanks will be able to use all their personal 
    cooldowns to mitigate *Solar Ray* without additional help.
  - If you do *not* have a WAR, then the tanks will need to alternate who uses
    their 3rd vs 30% mitigations (MT uses 3rd first, ST uses 30% first). The
    tank that does not use their 30% mitigation will need *Reprisal* and two
    other 10% mitigations from the healers and/or D4 to survive.
- Each Run Dynamis needs both tank 90s, H2 30s, D3's party mitigation,
  *Reprisal*, *Feint*, and shields to survive.
  - It is expected that all tanks + D3 use their 90s mitigations when the
    second *Solar Ray* hit lands just before Run Dynamis (Delta Version). This
    will catch Run Dynamis (Delta Version) at the tail end, and be back off
    cooldown in time for Run Dynamis (Sigma Version).
  - A single player cannot *Feint* all three *Run Dynamis*, hence why we
    alternate between D1 and D2's *Feint*.
- *Reprisal* will be available for each *Solar Ray* and *Run Dynamis*. However,
  if the tanks are going to mitigate *Solar Ray*, the MT should use their 
  *Reprisal* on *Solar Ray*, leaving the ST to *Reprisal* the *Run Dynamis*.
- Healer mitigations and D4's *Addle* are free to be used wherever appropriate.

<table>
  <tr>
    <td>
      <p>Solar Ray #1</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Hallowed Ground > Superbolide > full mits + swap</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Run Dynamis (Delta Version)</p>
      <ul>
        <li><b>P:</b> 131k-145k</li>
        <li><b>M:</b> 122k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal, ST 90s, H2 30s, D1, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST 90s, D3 should be used at the second Solar Ray
        hit for them to be back for <em>Run Dynamis (Sigma Version)</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Solar Ray #2</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Superbolide > Living Dead > full mits + swap</li>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Run Dynamis (Sigma Version)</p>
      <ul>
        <li><b>P:</b> 131k-145k</li>
        <li><b>M:</b> 122k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal, ST 90s, H2 30s, D2, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Solar Ray #3</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>
          <p>Holmgang > mitigate + swap</p>
          <p>If no WAR:</p>
          <ul>
            <li><b>MT:</b> Rampart + 3rd + short</li>
            <li><b>ST:</b> 30% + Rampart + short</li>
          </ul>
        </li>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>If this is not taken by <em>Holmgang</em>, both tanks will need to
        pop <em>Rampart</em> when the arm lasers resolve.</li>
        <li>Healers help the MT with mitigation.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Run Dynamis (Omega Version)</p>
      <ul>
        <li><b>P:</b> 131k-145k</li>
        <li><b>M:</b> 122k-135k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST Reprisal, ST 90s, H2 30s, D1, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Solar Ray #4</p>
      <ul>
        <li><b>T:</b> 242k-307k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><p>Mitigate + swap</p>
          <p>If no WAR:</p>
          <ul>
            <li><b>MT:</b> 30% + Rampart + short</li>
            <li><b>ST:</b> Rampart + 3rd + short</li>
          </ul>
        </li>
        <li>MT Reprisal</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Healers help the ST with mitigation.</li>
        <li>If H1 uses their 120s here, it will be back up just in time for 
        <em>Cosmo Dive</em> in P6.</li>
      </ul>
    </td>
  </tr>
</table>

### P6. Alpha Omega

There isn't too much wiggle room in this phase given how hard everything hits,
however, there are still some points worth mentioning.

- *Feint* does not actually change any breakpoints in the worst case scenario,
  so its inclusion is just for comfort. It makes a small difference at
  *Cosmo Meteor's* Flares, where a *Feint* with a *Zoe* ensures survival even
  with high rolls.
- Be careful about applying debuffs on the boss during *Wave Cannon's* spreads,
  for you risk not having LB3 at *Cosmo Dive* 2.

<table>
  <tr>
    <td>
      <p>Cosmo Memory</p>
      <p><em>(after tank LB3)</em></p>
      <ul>
        <li><b>P:</b> 74k-82k</li>
        <li><b>M:</b> 69k-76k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT90s, ST Reprisal, H2 30s, D1</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>Tank LB:</b> WAR > PLD > DRK > GNB</li>
        <li>The party actually just needs one piece of mitigation to survive
        Cosmo Memory after the Tank LB3- the other mitigations are to put them
        on cooldown so they are not accidentally used elsewhere, and to reduce
        the amount of healing needed to top the party back up.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Dive #1</p>
      <ul>
        <li><b>T:</b> 235k-286k</li>
        <li><b>P:</b> 94k-104k</li>
        <li><b>M:</b> 87k-96k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT + ST Rampart + 3rd + short</li>
        <li>MT Reprisal, H1 120s, H2 30s, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #1 (spread)</p>
      <ul>
        <li><b>P:</b> 84k-93k</li>
        <li><b>M:</b> 78k-86k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 30s, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #1 (stack)</p>
      <ul>
        <li><b>T:</b> 315k-370k</li>
        <li><b>P:</b> 102k-119k</li>
        <li><b>M:</b> 94k-110k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT:</b> 30% + short</li>
        <li><b>ST:</b> Invuln + give short to MT</li>
        <li>ST Reprisal, ST 90s, D2</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Also covered by H2 30s and D3.</li>
        <li>If the ST is a DRK or GNB, they can use their 90s to mitigate
        <em>Wave Cannon</em>'s spreads.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (spread)</p>
      <ul>
        <li><b>P:</b> 84k-93k</li>
        <li><b>M:</b> 78k-86k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 30s, H2 120s</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wave Cannon #2 (stack)</p>
      <ul>
        <li><b>T:</b> 315k-370k</li>
        <li><b>P:</b> 102k-119k</li>
        <li><b>M:</b> 94k-110k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>MT:</b> Invuln + give short to ST</li>
        <li><b>ST:</b> 30% + short</li>
        <li>MT Reprisal, MT 90s, D1</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Also covered by H2 30s and H2 120s.</li>
        <li>If the MT is a DRK or GNB, they can use their 90s to mitigate
        <em>Wave Cannon</em>'s spreads.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Dive #2</p>
      <ul>
        <li><b>T:</b> 235k-286k</li>
        <li><b>P:</b> 94k-104k</li>
        <li><b>M:</b> 87k-96k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Rampart + 3rd + short</li>
        <li>ST Reprisal, H2 30s, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Meteor (Meteors)</p>
      <ul>
        <li><b>P:</b> 101k-112k</li>
        <li><b>M:</b> 94k-106k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s, H1 120s, H2 30s, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Cosmo Meteor (Flares)</p>
      <ul>
        <li><b>P:</b> 73k-90k</li>
        <li><b>M:</b> 64k-85k</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>H2 90s, D2</li>
      </ul>
    </td>
    <td></td>
  </tr>
</table>

## Mitigation by Role

### MT

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li><em>Reprisal</em> to cover the 1st and 2nd waves.</li>
        <li>MT 90s where appropriate.
          <ul>
            <li>DRK/GNB should use their tank 90s at the 1st or 2nd wave.</li>
          </ul>
        </li>
      </ul>
      <p><b>Diffused Wave Cannon Kyrios</b> (Pantokrator)</p>
      <ul>
        <li>Invuln. You will need to time the invuln on the fifth pulse.</li>
      </ul>
      <p>Use <em>Rampart</em> when Omega becomes untargetable.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p><b>Solar Ray</b></p>
      <ul>
        <li><em>Rampart</em> + short.</li>
      </ul>
      <p><b>Optimized Bladedance (tethers)</b></p>
      <ul>
        <li>30% + <em>Rampart</em> + 3rd + short.</li>
      </ul>
      <p><b>Pile Pitch + Meteors</b></p>
      <ul>
        <li>90s party mits</li>
        <ul>
          <li>WAR/PLD can use their 90s as early as when the <em>Packet
          Filters</em> drop at the start of <em>Limitless Synergy</em>.</li>
          <li>GNB/DRK should wait for <em>Beyond Defense</em>'s kick to use
          their 90s to also cover <em>Cosmo Memory</em>.</li>
        </ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p><b>Hello, World</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Towers #1</b></p>
      <ul>
        <li>90s party mits.
          <ul>
            <li>WAR/PLD can use their party mits early to get an extra use at
            <em>Critical Error</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Towers #3</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p><b>Wave Cannon #1 (spread)</b></p>
      <ul>
        <li><em>Reprisal</em> to cover the spread + stack.</li>
      </ul>
      <p>You cannot use your 90s party mitigations, as they will be needed for
      <em>Run Dynamis</em>.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p><b>Solar Ray</b></p>
      <p>How the party resolves <em>Solar Ray</em> will depend on what tanks
      the party has.</p>
      <ul>
        <li><em>Reprisal</em> the Solar Rays that will be mitigated.</li>
        <li><p>If there is a WAR:</p>
          <ol>
            <li>Hallowed Ground > Superbolide > full mits + swap</li>
            <li>Living Dead > full mits + swap</li>
            <li>Holmgang</li>
            <li>Full mits + swap</li>
          </ol>
        </li>
        <li><p>If there isn't a WAR:</p>
          <ol>
            <li>Hallowed Ground > Superbolide</li>
            <li>Superbolide > Living Dead</li>
            <li>Reprisal, Rampart, 3rd, short + swap</li>
            <li>Reprisal, 30%, Rampart, short + swap</li>
          </ol>
        </li>
      </ul>
      <p><b>Run Dynamis</b> (all)</p>
      <ul>
        <li>MT 90s
          <ul>
            <li>You will need to use your MT 90s at the second <em>Solar 
            Ray</em> hit before <em>Run Dynamis (Delta Version)</em>. WAR/PLD 
            can use their 90s as soon as Omega-M is targetable.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p>The two tanks will invuln the two <em>Wave Cannon</em> stacks.</p>
      <p><b>Cosmo Memory</b></p>
      <ul>
        <li>Tank LB3
          <ul>
            <li>Priority: <em>WAR > PLD > DRK > GNB</em></li>
          </ul>
        </li>
        <li>MT 90s
          <ul>
            <li>This isn't strictly needed for survival, but it reduces the
            amount of healing the healers need to do after Cosmo Memory, and 
            puts the 90s party mitigation on cooldown so it's not accidentally
            used at the wrong place.</li>
          </ul>
        </li>
      </ul>
      <p><b>Cosmo Dive #1</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd, short</li>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Wave Cannon #1</b></p>
      <ul>
        <li>30%, short</li>
      </ul>
      <p><b>Wave Cannon #2</b></p>
      <ul>
        <li>Invuln</li>
        <li><em>Reprisal</em>, MT 90s
        </li>
        <li>Give short mit to the ST.</li>
      </ul>
      <p><b>Cosmo Dive #2</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd, short</li>
      </ul>
      <p><b>Cosmo Meteor</b></p>
      <ul>
        <li><em>Reprisal</em>
          <ul>
            <li>Use <em>Reprisal</em> when the AoEs in the center resolve to
            catch both Meteor waves.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

### ST

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li><em>Reprisal</em> to cover the 3rd and 4th waves.</li>
        <li>ST 90s where appropriate.
          <ul>
            <li>DRK/GNB should use their tank 90s at the 1st or 2nd wave.</li>
          </ul>
        </li>
      </ul>
      <p><b>Diffused Wave Cannon Kyrios</b> (Pantokrator)</p>
      <ul>
        <li>Invuln. You will need to time the invuln on the fifth pulse.</li>
      </ul>
      <p>Use <em>Rampart</em> when Omega becomes untargetable.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p><b>Solar Ray</b></p>
      <ul>
        <li><em>Rampart</em> + short.</li>
      </ul>
      <p><b>Optimized Bladedance (tethers)</b></p>
      <ul>
        <li>30% + <em>Rampart</em> + 3rd + short.</li>
      </ul>
      <p><b>Pile Pitch + Meteors</b></p>
      <ul>
        <li>90s party mits</li>
        <ul>
          <li>WAR/PLD can use their 90s as early as when the Packet Filters 
          drop at the start of <em>Limitless Synergy</em>.</li>
          <li>GNB/DRK should wait for <em>Beyond Defense</em>'s kick to use 
          their 90s to also cover <em>Cosmo Memory</em>.</li>
        </ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p><b>Towers #1</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Towers #3</b></p>
      <ul>
        <li><em>ST 90s</em></li>
      </ul>
      <p><b>Towers #4</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p><b>Wave Cannon #2 (spread)</b></p>
      <ul>
        <li><em>Reprisal</em> to cover the spread + stack.</li>
      </ul>
      <p>You cannot use your 90s party mitigations, as they will be needed for
      <em>Run Dynamis</em>.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p><b>Solar Ray</b></p>
      <p>How the party resolves <em>Solar Ray</em> will depend on what tanks
      the party has.</p>
      <ul>
        <li>Let the MT <em>Reprisal</em> Solar Rays- your priority are the 
        <em>Run Dynamis</em>.</li>
        <li><p>If there is a WAR:</p>
          <ol>
            <li>Hallowed Ground > Superbolide > full mits + swap</li>
            <li>Living Dead > full mits + swap</li>
            <li>Holmgang</li>
            <li>Full mits + swap</li>
          </ol>
        </li>
        <li><p>If there isn't a WAR:</p>
          <ol>
            <li>Hallowed Ground > Superbolide</li>
            <li>Superbolide > Living Dead</li>
            <li>Reprisal, 30%, Rampart, short + swap</li>
            <li>Reprisal, Rampart, 3rd, short + swap</li>
          </ol>
        </li>
      </ul>
      <p><b>Run Dynamis</b> (all)</p>
      <ul>
        <li><em>Reprisal</em>, ST 90s
          <ul>
            <li>You will need to use your ST 90s at the second <em>Solar 
            Ray</em> hit before <em>Run Dynamis (Delta Version)</em>. WAR/PLD 
            can use their 90s as soon as Omega-M is targetable.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p>The two tanks will invuln the two <em>Wave Cannon</em> stacks.</p>
      <p><b>Cosmo Memory</b></p>
      <ul>
        <li>Tank LB3
          <ul>
            <li>Priority: <em>WAR > PLD > DRK > GNB</em></li>
          </ul>
        </li>
        <li><em>Reprisal</em>
          <ul>
            <li>This isn't strictly needed for survival, but it reduces the
            amount of healing the healers need to do after Cosmo Memory, and 
            puts <em>Reprisal</em> on cooldown so it's not accidentally used at
            the wrong place.</li>
          </ul>
        </li>
      </ul>
      <p><b>Cosmo Dive #1</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd, short</li>
      </ul>
      <p><b>Wave Cannon #1</b></p>
      <ul>
        <li>Invuln</li>
        <li><em>Reprisal</em>, ST 90s</li>
        <li>Give short mit to the MT.</li>
      </ul>
      <p><b>Wave Cannon #2</b></p>
      <ul>
        <li>30% + short</li>
      </ul>
      <p><b>Cosmo Dive #2</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd, short</li>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Cosmo Meteor</b></p>
      <ul>
        <li>ST 90s</li>
      </ul>
    </td>
  </tr>
</table>

### H1

This assumes your H1 is either a WHM or AST. As double barrier healer parties
are fairly common, adapt this as needed if H1 is a SCH or SGE.

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li>H1 120s
          <ul>
            <li>This can cover all four waves, if timed correctly.</li>
          </ul>
        </li>
        <li>H1s will also typically use their H1 180s abilities here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p>The ST will take more damage than the MT after <em>Party Synergy</em>.</p>
      <p><b>Pile Pitch + Meteors</b></p>
      <ul>
        <li>H1 120s</li>
        <ul>
          <li>The earliest a WHM can use <em>Temperance</em> and still cover
          <em>Cosmo Memory</em> is when the Flare markers appear.</li>
        </ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p>H1 180s abilities can be used at any tower.</p>
      <p><b>Towers #2</b></p>
      <ul>
        <li>H1 120s
        <ul>
          <li>Depending on when a WHM used <em>Temperance</em> in P2, and when
          Omega-F was defeated, <em>Temperance</em> may not be available. If so, 
          consider holding <em>Temperance</em> for P4, and substitute with
          <em>Liturgy of the Bell</em>.</li>
        </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p>The healers are primarily responsible for mitigating and healing this
      phase.</p>
      <ul>
        <li>Use H1 120s at either the 1st or 2nd Wave Cannon spread.
          <ul>
            <li>This will cover two spreads, and two stacks.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p>H1 is not responsible for mitigating any <em>Run Dynamis</em>.</p>
      <ul>
        <li>This means you are free to use your H1 120s anywhere in P5 where
        appropriate (including mitigating <em>Run Dynamis</em> if you choose.)</li>
      </ul>
      <p><b>Solar Ray</b></p>
      <p>How the party resolves <em>Solar Ray</em> will depend on what tanks
      the party has.</p>
      <p>If the party does not have a WAR, then you will need to help the tanks 
      mitigate the two <em>Solar Rays</em> before and after <em>Run Dynamis 
      (Omega Version)</em>.</p>
      <p>This can be done either via H1 120s, or 
      <em>Aquaveil/Exaltation</em>.</p>
      <ol>
        <li>Invulned</li>
        <li>Invulned</li>
        <li>Help the MT</li>
        <li>Help the ST</li>
      </ol>
      <p>H1 will typically use their H1 180s abilities at the front part of
      <em>Run Dynamis (Delta Version)</em> to help heal the first set of
      tether break, Beyond Defense/Pile Pitch, and monitors.</p>
      <ul>
        <li>H1 180s used when the outer spinning hands appear (before the spin 
        indicators) will cover up to <em>Oversampled Wave Cannon</em> 
        (monitors).</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p>The two healers will need to decide who goes center during <em>Cosmo 
      Meteor</em>.</p>
      <p><b>Cosmo Dive #1</b></p>
      <ul>
        <li>H1 120s</li>
      </ul>
      <p><b>Cosmo Meteor</b></p>
      <ul>
        <li>H1 120s
          <ul>
            <li>A WHM should use <em>Temperance</em> when the baited AoEs
            resolve- it is 19 seconds from the first set of Meteors until the 
            Flares, and a well-timed <em>Temperance</em> will be able to
            mitigate all of <em>Cosmo Meteor</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

### H2

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li>H2 120s
          <ul>
            <li>This can cover all four waves, if timed correctly.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p>H2 30s are used at Meteors, but you can get additional uses at:</p>
      <ul>
        <li>The <em>Solar Rays</em> at the start to help the tanks mitigate
        both <em>Solar Ray</em> at the follow-up auto-attacks.</li>
        <li>Immediately after <em>Party Synergy</em> to mitigate auto-attacks
        (especially for the ST).</li>
      </ul>
      <p>The ST will take more damage than the MT after <em>Party Synergy</em>.</p>
      <p><b>Pile Pitch + Meteors</b></p>
      <ul>
        <li>H2 30s, H2 90s, H2 120s</li>
        <ul>
          <li>Use your H2 30s when the kick from <em>Beyond Defense</em> 
          happens.</li>
          <li>The earliest you can deploy boosted shields via H2 90s and still
          catch Meteors is when <em>Limitless Synergy</em> finishes its cast.</li>
          <li>The earliest you can use your H2 120s and still cover <em>Cosmo 
          Memory</em> is when the Flare markers appear.</li>
          <li><em>Seraph/Panhaima</em> is typically used to mitigate the
          Meteors and <em>Cosmo Memory</em>.</li>
        </ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p>This phase is left unstructured with the exception of 2nd towers, as
      that is the only time you can use H2 120s to mitigate and still have them
      available for P4.</p>
      <p>Each round of towers needs three pieces of mitigation (shields count)
      for the party to survive one whole round without any healing in between.</p>
      <ul>
        <li>The rest of the party will cover 2/3 of these, so you have the
        flexibility to add the last however you see fit. For example:
          <ol>
            <li>H2 30s</li>
            <li>H2 120s</li>
            <li>H2 30s</li>
            <li><em>Seraph/Panhaima</em></li>
          </ol>
        </li>
      </ul>
      <p><b>Transition</b></p>
      <ul>
        <li>The party <em>must</em> have at least shields to survive.</li>
      </ul>
      <p><b>Hello, World</b></p>
      <ul>
        <li>This doesn't actually need H2 30s, although you can cover both
        <em>Hello, World</em> and the first set of towers if H2 30s is used 
        before Omega is targetable.</li>
      </ul>
      <p><b>Towers #1</b></p>
      <ul>
        <li>A lot of H2s will use their H2 90s here.</li>
      </ul>
      <p><b>Towers #2</b></p>
      <ul>
        <li>H2 120s</li>
      </ul>
      <p><b>Critical Error</b></p>
      <ul>
        <li>This needs either shields + H2 30s or H2 90s.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p>The healers are primarily responsible for mitigating and healing this
      phase.</p>
      <ul>
        <li>Use H2 120s at either the 1st or 2nd Wave Cannon spread.
          <ul>
            <li>SCH's <em>Expedient</em> is particularly useful at the 1st
            Wave Cannon stack.</li>
            <li>This will cover two spreads, and two stacks.</li>
          </ul>
        </li>
        <li>The latest you can use H2 30s and have it back by <em>Blue
        Screen</em> is at the 2nd stack.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p><b>Run Dynamis</b> (all)</p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p>You are free to use your H2 120s and <em>Seraph/Panhaima</em>
      anywhere in P5 where appropriate (including mitigating <em>Run
      Dynamis</em> if you choose.)</p>
      <p><b>Solar Ray</b></p>
      <p>How the party resolves <em>Solar Ray</em> will depend on what tanks
      the party has.</p>
      <p>If the party does not have a WAR, then you will need to help the tanks 
      mitigate the two <em>Solar Rays</em> before and after <em>Run Dynamis 
      (Omega Version)</em>.</p>
      <p>This can be done either via H2 120s, or 
      <em>Taurochole/Protraction</em>.</p>
      <ol>
        <li>Invulned</li>
        <li>Invulned</li>
        <li>Help the MT</li>
        <li>Help the ST</li>
      </ol>
      <p>H2 30s can be used to help the tanks mitigate the final <em>Solar
      Ray</em> after <em>Run Dynamis (Omega Version)</em>.</p>
      <p><em>Blind Faith</em> will require shields for the party to survive.</p>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p>The two healers will need to decide who goes center during <em>Cosmo 
      Meteor</em>.</p>
      <p>The published mitplan doesn't account for <em>Seraph/Panhaima</em>,
      or <em>Fey Illumination</em>. These can either be used at either
      <em>Wave Cannon</em>, or at <em>Cosmo Dive #1</em> + <em>Cosmo Meteor</em>.</p>
      <p>Because SCH also has access to <em>Fey Illumination</em>, an 
      alternative plan would be to use <em>Expedient</em> for <em>Cosmo Dive 
      #1</em> and <em>Cosmo Meteor</em>, and use <em>Fey Illumination</em> (and
      possibly <em>Dissipation</em>) to cover <em>Wave Cannon</em> #2.</p>
      <p><b>Cosmo Memory</b></p>
      <ul>
        <li>This needs either shields or H2 30s in addition to the tank LB3.
        Other members of the party may also mitigate this, if so, then you
        won't need to do anything.</li>
      </ul>
      <p><b>Cosmo Dive #1</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Wave Cannon #1</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>Use H2 30s after dodging all the Exaflares.</li>
          </ul>
        </li>
      </ul>
      <p>A SCH can summon <em>Seraph</em> when the first baited AoEs appear to
      have <em>Consolation</em> cover both the spread + stack, and be back in 
      time to cover <em>Cosmo Meteor's</em> Flares.</p>
      <p>It is also common practice to use the H2 90s to cover <em>Wave Cannon</em>
      #1's spreads, as it will be back in time for <em>Cosmo Meteor</em>.</p>
      <p><b>Wave Cannon #2</b></p>
      <ul>
        <li>H2 30s, H2 120s
          <ul>
            <li>Use H2 30s when <em>Wave Cannon</em>'s cast starts. This will 
            be while dodging <em>Cosmo Arrow</em>.</li>
            <li>The earliest you can use H2 120s is when the first <em>Cosmo
            Arrow</em> lines resolve.</li>
            <li>Some SCH will choose to replace the <em>Expedient</em> here
            with <em>Fey Illumination</em> instead.</li>
          </ul>
        </li>
      </ul>
      <p><b>Cosmo Dive #2</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>The earliest you can use H2 30s is when the fourth Exaflare
            telegraphs appear (when you turn left or right when baiting AoEs).</li>
            <li>You may want to use H2 30s early here to have the H2 30s back
            up in time for the first wave of Meteors.</li>
          </ul>
        </li>
      </ul>
      <p><b>Cosmo Meteors (Meteors)</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>Depending on when the H2 30s was used at <em>Cosmo Dive #2</em>,
            it may not be up in time to catch the first wave of Meteor hits.
            However, this is covered by the ST 90s (even if WAR/PLD). You will
            need H2 30s to cover the second wave if the ST is WAR or PLD.</li>
          </ul>
        </li>
      </ul>
      <p><b>Cosmo Meteors (Flares)</b></p>
      <ul>
        <li>H2 90s
          <ul>
            <li>Not strictly necessary, since you just need a small boost to
            regular shields here. <em>Consolation/Panhaima</em> is an 
            appropriate substitute.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

### D1

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li><em>Feint</em> will cover two waves. You can work with D2, and 
        cover the first two waves with your <em>Feint</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p>There aren't any great places to use <em>Feint</em> in this phase, as
      all the major raid-wides come from untargetable sources.</p>
      <p>Thus, <em>Feint's</em> best use is to mitigate the auto-attacks after
      <em>Party Synergy</em> (assuming you used <em>Feint</em> in P1.)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p><b>Hello, World</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Critical Error</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p>As you will be mitigating <em>Run Dynamis (Delta Version)</em>, you
      cannot use <em>Feint</em> anywhere in this phase.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p><b>Run Dynamis (Delta Version)</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Run Dynamis (Omega Version)</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p><b>Cosmo Memory</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>This isn't strictly needed, and is more to get an extra use,
            and to put <em>Feint</em> on cooldown so it's not accidentally used
            at the wrong place.</li>
          </ul>
        </li>
      </ul>
      <p><b>Wave Cannon #2 (stack)</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>You <em>can</em> also mitigate the spreads if timed correctly,
            however, if too many debuffs are applied on the boss during the 
            spreads, the party will not build LB gauge, and this will cause the
            party to only have LB2 when it's time to melee LB3 at <em>Cosmo 
            Dive #2</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

### D2

This assumes D2 is a melee DPS.

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li><em>Feint</em> will cover two waves. You can work with D1, and 
        cover the third and fourth waves with your <em>Feint</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p>There aren't any great places to use <em>Feint</em> in this phase, as
      all the major raid-wides come from untargetable sources.</p>
      <p>Thus, <em>Feint's</em> best use is to mitigate the auto-attacks after
      <em>Party Synergy</em> (assuming you used <em>Feint</em> in P1.)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p>Your <em>Feint</em> doesn't actually change any breakpoints with a
      high roll during the towers, hence it is not part of the mitigation 
      framework.</p>
      <p>As such, feel free to use your <em>Feint</em> at any tower, although
      D1 has their <em>Feint</em> at <em>Hello, World</em> and <em>Critical 
      Error</em>.</p>
      <p>Alternatively, you can also use <em>Feint</em> to help mitigate
      Omega's auto-attacks in between tower sets.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p>You can use <em>Feint</em> anywhere in this phase. The better places
      would either be at the third <em>Wave Cannon</em> spread, or at <em>Blue
      Screen</em>.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p><b>Run Dynamis (Sigma Version)</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Solar Ray #4</b> (after Omega)</p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>Not strictly necessary, but nice to have, especially if the
            party doesn't have a WAR.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p><b>Wave Cannon #1 (stack)</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>You <em>can</em> also mitigate the spreads if timed correctly,
            however, if too many debuffs are applied on the boss during the 
            spreads, the party will not build LB gauge, and this will cause the
            party to only have LB2 when it's time to melee LB3 at <em>Cosmo 
            Dive #2</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Cosmo Meteor (Flares)</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>This is to help guard against a high-roll (or if someone
            happens to be a bit too close).</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

### D3

Notably, because MCH has *Dismantle* for on-demand mitigation, there are some
modifications that are available to MCH that are not available to BRD or DNC.

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li>D3 party mitigation will cover three waves if timed correctly. Use 
        your party mitigation at either the first, or second wave.</li>
        <li>MCH can split <em>Tactician</em> and <em>Dismantle</em> to cover 
        all four waves. <em>Dismantle</em> will cover two waves.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p><b>Pile Pitch + Meteors → Cosmo Memory</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
        <ul>
          <li>Wait for <em>Beyond Defense</em>'s kick to use your party 
          mitigation to also cover <em>Cosmo Memory</em>.</li>
        </ul>
      </ul>
      <p>A BRD can use <em>Nature's Minne</em> to help H2's shields when
      <em>Limitless Synergy</em> is cast.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p>A DNC should start <em>Improvisation</em> when Omega-F is defeated in
      the previous phase to mitigate the transition.</p>
      <p><b>Towers #4</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
      <p>MCH can use <em>Tactician</em> or <em>Dismantle</em> to cover an
      extra set of towers in addition to the fourth set.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p>You will need to use your party mitigation for <em>Run Dynamis (Delta 
      Version)</em>, so you will not be mitigating this phase.</p>
      <p>However, a MCH can <em>Tactician</em> here and save <em>Dismantle</em>
      for <em>Run Dynamis (Delta Version)</em>. If so, use <em>Tactician</em>
      just before the second <em>Wave Cannon</em> stack, as this would mitigate
      two stacks (which do more damage than spreads).</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p><b>Run Dynamis</b> (all)</p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>You will need to use your party mitigations at the second 
            <em>Solar Ray</em> hit before <em>Run Dynamis (Delta
            Version)</em>.</li>
            <li>MCH can substitute <em>Dismantle</em> for <em>Tactician</em>,
            although you cannot <em>Dismantle</em> two consecutive <em>Run 
            Dynamis</em>.</li>
          </ul>
        </li>
      </ul>
      <p>MCH can use <em>Dismantle</em> in other places, particularly during
      <em>Solar Ray</em> if the party doesn't have a WAR. You may want to check
      with your D4 if they are going to <em>Addle</em> a <em>Solar Ray</em>,
      and <em>Dismantle</em> the one they don't choose.</p>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p><b>Wave Cannon #1</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>Use <em>Troubadour/Tactician/Shield Samba</em> after dodging
            all the Exaflares.</li>
          </ul>
        </li>
      </ul>
      <p><b>Cosmo Meteor (Meteors)</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>Use this when the baited AoE telegraphs appear (and the party
            is still together.)</li>
          </ul>
        </li>
      </ul>
      <p>A MCH can use <em>Dismantle</em> anywhere in this phase- the most
      typical use would be at <em>Wave Cannon #2's</em> stack.</p>
      <p><b>Do not</b> use <em>Dismantle</em> at <em>Wave Cannon's</em>
      spread, as it can lead to the party applying too many debuffs during this
      time, causing the party to not build LB gauge and only have LB2 when it's
      time to melee LB3 at <em>Cosmo Dive #2</em>.</p>
    </td>
  </tr>
</table>

### D4

<table>
  <tr>
    <td>
      <p><b>P1. Omega</b></p>
    </td>
    <td>
      <p><b>Condensed Wave</b> (Pantokrator)</p>
      <ul>
        <li><em>Addle</em> will cover two waves. Use it at any of the first
        three waves.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Omega-M/F</b></p>
    </td>
    <td>
      <p>There aren't any great places to use <em>Addle</em> in this phase, as
      all the major raid-wides come from untargetable sources.</p>
      <p>Thus, the best use of <em>Addle</em> is to mitigate Omega-F's 
      auto-attacks after <em>Party Synergy</em>.</p>
      <p>A RDM can use <em>Magick Barrier</em> at either Meteors, or <em>Cosmo 
      Memory</em>. If the party's tanks are WAR + PLD, use <em>Magick
      Barrier</em> at <em>Cosmo Memory</em>.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Omega Reconfigured</b></p>
    </td>
    <td>
      <p><b>Hello, World</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p><b>Critical Error</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Blue Screen</b></p>
    </td>
    <td>
      <p>Because D4 isn't responsible for mitigating P5, you are free to use 
      <em>Addle</em> anywhere in this phase if you give up <em>Addle</em> at 
      <em>Run Dynamis (Delta Version)</em>.</p>
      <p>If so, use <em>Addle</em> to mitigate the third <em>Wave Cannon</em> 
      spread + stack, as the tanks have the first two covered with
      <em>Reprisal</em>.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Run Dynamis</b></p>
    </td>
    <td>
      <p>The mitigation plan for this phase doesn't include <em>Addle</em>, 
      as <em>Addle</em> is not available for all three <em>Run Dynamis</em>.</p>
      <p>As such, you are free to use <em>Addle</em> (and <em>Magick
      Barrier</em>) anywhere in this phase.</p>
      <p>If the party does not have a WAR, <em>Addle</em> is particularly
      helpful at helping the tanks mitigate the <em>Solar Ray</em> before
      <em>Run Dynamis (Omega Version)</em>. You cannot <em>Addle</em> both, and
      H2 can use H2 30s for the <em>Solar Ray</em> after.</p>
    </td>
  </tr>
  <tr>
    <td><b>P6. Alpha Omega</b></td>
    <td>
      <p><b>Cosmo Dive #1</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p><b>Cosmo Dive #2</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p>A RDM would typically use <em>Magick Barrier</em> at <em>Wave Cannon
      #2</em>'s stack.</p>
    </td>
  </tr>
</table>
