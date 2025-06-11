---
layout: default
title: A. Mitigation
parent: Lv 100. FRU (Mana)
nav_order: 9
has_children: false
has_toc: false
permalink: /ultimates/fru/mitigation/
---

# Appendix A: Mitigation

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
        <li><a href="#p1-fatebreaker">P1. Fatebreaker</a></li>
        <li><a href="#p2-usurper-of-frost">P2. Usurper of Frost</a></li>
        <li><a href="#p3-oracle-of-darkness">P3. Oracle of Darkness</a></li>
        <li><a href="#p4-gaia-and-shiva">P4. Gaia and Shiva</a></li>
        <li><a href="#p5-pandora">P5. Pandora</a></li>
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
    <td>Tank 40%</td>
    <td>Damnation, Guardian, Shadowed Vigil, Great Nebula</td>
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
    <td>Temperance/Divine Grace, Neutral Sect/Sunsign</td>
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
    <td>H2 180s</td>
    <td>Seraphism, Philosophia</td>
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

- Tanks have 225k max HP.
- Physical DPS jobs have 157k max HP.
- Magical jobs have 142k max HP.
- Basic shields *(Concitation, Eukrasian Prognosis II)* absorb 20k damage.

### P1. Fatebreaker

<table>
  <tr>
    <td>
      <p>Powder Mark Trail #1</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, D1, D3, D4</li>
        <li>MT 40%, Rampart, short</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><em>Rampart</em> should be used towards the end of the castbar, as
        we want it to cover <em>Burn Mark</em> as well.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Burn Mark</p>
    </td>
    <td>
      <ul>
        <li>MT Rampart, MT 3rd, ST short</li>
        <li>ST Rampart, ST 3rd, ST 40%</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Covered by MT Rampart.</li>
        <li>The ST gives the MT their short personal mitigations here, because
        the MT 40% was used to cover <em>Powder Mark Trail</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Burnished Glory #1</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, H1 120, H2 120s, H2 30s, D2</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Healer 120s mitigations can be used right after the knockback, and
        will last to <em>Burnished Glory</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Burnished Glory #2</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, MT 90s, ST 90s, H2 30s, D1, D3, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>15s mitigations (like <em>Reprisal</em>, <em>Tactician</em>,
        <em>Heart of Light</em>, etc.) should be applied after the second
        tether resolves, which will cover the last two tethers in addition to
        <em>Burnished Glory</em>.</li>
        <li>Shields, like <em>Shake It Off</em> and <em>Divine Veil</em> should
        be saved for <em>Burnished Glory</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Powder Mark Trail #2</p>
    </td>
    <td>
      <ul>
        <li>PLD > ST Invuln</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A PLD MT must <em>Hallowed Ground</em> this <em>Powder Mark
        Trail</em> for <em>Hallowed Ground</em> to be back in time for P3.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Burn Mark</p>
    </td>
    <td>
      <ul>
        <li>MT Rampart, MT 40%, MT 30%</li>
        <li>ST Rampart, ST 3rd, ST short</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The MT gives the ST their short personal mitigations this time,
        since the ST doesn't have 40% available.</li>
      </ul>
    </td>
  </tr>
</table>

### P2. Usurper of Frost

<table>
  <tr>
    <td>
      <p>Quad Slap</p>
    </td>
    <td>
      <ul>
        <li>MT invuln</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A PLD <em>cannot</em> <em>Hallowed Ground</em> this, or they lose a
        use over the entire fight (P3 and P5).</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Diamond Dust</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, H2 30s, H2 120s, D2, D4</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>Akh Morn</td>
    <td>
      <ul>
        <li>H1 120s, MT 90s, ST 90s</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Hallowed Ray</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, H2 30s, D1</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Any "extra" mitigations <em>(Magick Barrier, Passage of Arms, etc.)</em>
        should be used here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Light Rampant</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, H2 30s, D2, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Mitigations and debuffs that last 15 seconds can cover both the
        <em>Banish III</em> at the end of <em>Mirror, Mirror</em> and <em>Light
        Rampant</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>House of Light</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, MT 90s, H2 120s</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Absolute Zero</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s, H1 120s, H2 30s</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
</table>

### P3. Oracle of Darkness

<table>
  <tr>
    <td>
      <p>Ultimate Relativity</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, H1 120s, H2 120s, D1, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The healer 120s are here so that they're back in time for the final
        <em>Shockwave Pulsar → Memory's End</em> sequence.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Fire/Unholy Darkness #1</p>
    </td>
    <td>
    </td>
    <td>
      <ul>
        <li>Covered by H1 120s and H2 120s from <em>Ultimate Relativity</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Fire/Unholy Darkness #2</p>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST 90s</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Fire/Unholy Darkness #3</p>
    </td>
    <td>
      <ul>
        <li>D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Covered by MT 90s and ST 90s from <em>Fire/Unholy Darkness #2</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Shell Crusher → Shockwave Pulsar</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, H2 30s</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Black Halo</p>
    </td>
    <td>
      <ul>
        <li>MT + ST Rampant + 40% + + 3rd + short.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>A tank can solo this with full mitigations, but there's no reason
        to do so.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Darkest Dance</p>
    </td>
    <td>
      <ul>
        <li>PLD > ST invuln</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Shockwave Pulsar</p>
    </td>
    <td>
      <ul>
        <li>H1 120s, H2 120s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Use 20s mitigations just before the cast resolves to have them
        cover <em>Memory's End</em> as well.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Memory's End</p>
    </td>
    <td>
      <ul>
        <li>H2 30s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Covered by H1 120s and H2 120s.</li>
      </ul>
    </td>
  </tr>
</table>

### P4. Gaia and Shiva

- The main mitigation point here is *Crystallize Time*. Because the sequence
  from getting stunned to the knockback is just under 15 seconds, we reserve
  both healer 120s mitigations for this because they last 20s each and have
  the largest margin of error.

<table>
  <tr>
    <td>
      <p>Darklit Dragonsong</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, MT 90s, ST 90s, D1, D3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Debuffs should target the <em>Usurper of Frost</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Somber Dance</p>
    </td>
    <td>
      <ul>
        <li>MT invuln</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Akh Morn #1</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, H2 30s</li>
        <li>MT Rampart, 3rd, short</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Morn Afah #1</p>
    </td>
    <td>
      <ul>
        <li>D2</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Covered by ST <em>Reprisal</em> and H2 30s from <em>Akh Morn</em>.</li>
        <li>Debuffs should target the <em>Usurper of Frost</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Crystallize Time</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, D4</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Debuffs should target the <em>Oracle of Darkness</em>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Hallowed Wings</p>
    </td>
    <td>
      <ul>
        <li>MT 90s, ST 90s, H1 120s, H2 120s, D3</li>
        <li>MT 40%, ST 40%</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>15s mitigations should be used right when the Oracle of Darkness
        does <em>Spirit Taker</em> right before the rewind.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Akh Morn #2</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, H2 30s</li>
        <li>ST Rampart, 3rd, short</li>
      </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      <p>Morn Afah #2</p>
    </td>
    <td>
    </td>
    <td>
      <ul>
        <li>Covered by ST <em>Reprisal</em> and H2 30s from <em>Akh Morn</em>.</li>
        <li>Debuffs should target the <em>Usurper of Frost</em>.</li>
      </ul>
    </td>
  </tr>
</table>

### P5. Pandora

<table>
  <tr>
    <td>
      <p>Fulgent Blade #1</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, MT 90s, D1</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Akh Morn #1</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, ST 90s, D2, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wings Dark and Light #1</p>
    </td>
    <td>
      <ul>
        <li>MT 40%, Rampart, short, 3rd</li>
        <li>ST 40%, Rampart, short, 3rd</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Tanks should use their short cds while dodging the Exalines to
        mitigate the boss's autoattacks. The latest you can use 25s mitigations
        and have them back for Wings Dark and Light would be around the second
        Exaline dodge.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Polarising Strikes #1</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, H1 120s, H2 120s, D3</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Pandora's Box</p>
    </td>
    <td>
      <ul>
        <li>Tank LB3</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>15s mitigations can cover both <em>Pandora's Box</em> and
        <em>Fulgent Blade</em> if used late enough (around the "B" in "Box").</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Fulgent Blade #2</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, MT 90s, D1</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Akh Morn #2</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s, D2, D4</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Wings Dark and Light #2</p>
    </td>
    <td>
      <ul>
        <li>MT + ST: Invuln</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Polarising Strikes #2</p>
    </td>
    <td>
      <ul>
        <li>ST Reprisal, H1 180s, H2 30s, H2 180s</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Fulgent Blade #3</p>
    </td>
    <td>
      <ul>
        <li>MT 90s, H1 120s, H2 120s</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Notably, H2 30s will not be back up in time.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Akh Morn #3</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, ST 90s, H2 30s, D2, D4</li>
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
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Cyclonic Break</b></p>
      <ul>
        <li><em>Reprisal</em> just before the cast bar finishes will last until
        <em>Powder Mark Trail</em>.</li>
        <li>If you are WAR or PLD, you can use <em>Shake It Off/Divine
        Veil</em> at the start and have it back for <em>Burnished Glory</em> #2.</li>
      </ul>
      <p><b>Powder Mark Trail #1</b></p>
      <ul>
        <li><em>Reprisal, Rampart</em>, 40%, short</li>
      </ul>
      <p>Use <em>Rampart</em> towards the end of the castbar to have it last to
      the <em>Burn Mark</em>.</p>
      <p><b>Burn Mark #1</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd</li>
      </ul>
      <p><b>Burnished Glory #1</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Burnished Glory #2</b></p>
      <ul>
        <li>MT 90s</li>
        <ul>
          <li>If you are a DRK or GNB, you can use <em>Dark Missionary/Heart of
          Light</em> after the second tether resolves to mitigate the third and
          fourth tethers in addition to <em>Burnished Glory</em>.</li>
        </ul>
      </ul>
      <p><b>Powder Mark Trail #2</b> (only if PLD MT)</p>
      <ul>
        <li><em>Hallowed Ground</em></li>
      </ul>
      <p><b>Burn Mark #2</b></p>
      <ul>
        <li><em>Rampart</em>, 40%, 3rd</li>
        <li>Give short mit to the ST.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Quad Strike</b></p>
      <ul>
        <li>Invuln</li>
      </ul>
      <p><b>Diamond Dust</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Sunburst Holy x4</b></p>
      <ul>
        <li>MT 90s</li>
      </ul>
      <p><b>Mirror, Mirror</b></p>
      <ul>
        <li>Rampart, 40%</li>
        <ul>
          <li>Cycle through these to mitigate auto-attacks.</li>
        </ul>
      </ul>
      <p><b>Banish III</b></p>
      <ul>
        <li><em>Reprisal</em></li>
        <ul>
          <li>Use this towards the end of the castbar to also cover <em>Light
          Rampant</em>.</li>
        </ul>
        <li>Give your short mit to D1 during Banish III.</li>
      </ul>
      <p><b>Light Rampant</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Absolute Zero</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Oracle of Darkness</b></p>
    </td>
    <td>
      <p><b>Ultimate Relativity</b></p>
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
      <p><b>P4. Gaia and Shiva</b></p>
    </td>
    <td>
      <p><b>Darklit Dragonsong</b></p>
      <ul>
        <li><em>Reprisal</em>, MT 90s</li>
      </ul>
      <p><b>Somber Dance</b></p>
      <ul>
        <li>Invuln</li>
        <li>Use <em>Rampart</em> when the boss jumps- this will cover <em>Akh
        Morn</em> #1 and be back for <em>Akh Morn</em> #2 in the event the ST
        dies.</li>
      </ul>
      <p><b>Akh Morn #1</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd, short</li>
      </ul>
      <p><b>Crystallize Time</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Hallowed Wings</b></p>
      <ul>
        <li>MT 90s, 40%</li>
      </ul>
      <p><b>Akh Morn #2</b></p>
      <ul>
        <li>Give short mit to the ST.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Pandora</b></p>
    </td>
    <td>
      <p><b>Fulgent Blade #1</b></p>
      <ul>
        <li><em>Reprisal</em>, MT 90s</li>
      </ul>
      <p><b>Wings Dark and Light #1</b></p>
      <ul>
        <li><em>Rampart</em>, 40%, 3rd, short</li>
      </ul>
      <p><b>Fulgent Blade #2</b></p>
      <ul>
        <li><em>Reprisal</em>, MT 90s</li>
      </ul>
      <p><b>Wings Dark and Light #2</b></p>
      <ul>
        <li>Invuln</li>
      </ul>
      <p><b>Fulgent Blade #3</b></p>
      <ul>
        <li><em>Reprisal</em>, MT 90s</li>
      </ul>
    </td>
  </tr>
</table>

### ST

<table>
  <tr>
    <td>
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Burn Mark #1</b></p>
      <ul>
        <li>40%, <em>Rampart</em>, 3rd</li>
        <li>Give the MT your targeted short mit.</li>
      </ul>
      <p><b>Burnished Glory #2</b></p>
      <ul>
        <li>ST Reprisal, ST 90s</li>
        <ul>
          <li>If you are a DRK or GNB, you can use <em>Dark Missionary/Heart of
          Light</em> after the second tether resolves to mitigate the third and
          fourth tethers in addition to <em>Burnished Glory</em>.</li>
        </ul>
      </ul>
      <p><b>Powder Mark Trail #2</b></p>
      <ul>
        <li><em>Invuln unless</em> you have a PLD MT (in which case, the PLD
        should take this with <em>Hallowed Ground</em> instead)</li>
      </ul>
      <p><b>Burn Mark #2</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd, short</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Sunburst Holy x4</b></p>
      <ul>
        <li>ST 90s</li>
      </ul>
      <p><b>Absolute Zero</b></p>
      <ul>
        <li>ST 90s</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Oracle of Darkness</b></p>
    </td>
    <td>
      <p><b>Fire/Unholy Darkness #2</b></p>
      <ul>
        <li><em>ST 90s</em></li>
      </ul>
      <p><b>Shockwave Pulsar #1</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Memory's End</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Gaia and Shiva</b></p>
    </td>
    <td>
      <p><b>Akh Morn #1</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Hallowed Wings</b></p>
      <ul>
        <li>ST 90s, 40%</li>
      </ul>
      <p><b>Akh Morn #2</b></p>
      <ul>
        <li><em>Rampart</em>, 3rd, short</li>
        <li><em>Reprisal</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Pandora</b></p>
    </td>
    <td>
      <p><b>Akh Morn #1</b></p>
      <ul>
        <li><em>Reprisal</em>, ST 90s</li>
      </ul>
      <p><b>Wings Dark and Light #1</b></p>
      <ul>
        <li><em>Rampart</em>, 40%, 3rd, short</li>
      </ul>
      <p><b>Fulgent Blade #2</b></p>
      <ul>
        <li><em>Reprisal</em></li>
        <ul>
          <li>This can also cover <em>Pandora's Box</em>.</li>
        </ul>
      </ul>
      <p><b>Wings Dark and Light #2</b></p>
      <ul>
        <li>Invuln</li>
      </ul>
      <p><b>Polarising Strikes #2</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Akh Morn #3</b></p>
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
      <p>You can use H2 90s to cover either <em>Wave Cannon</em>'s spreads. The
      latest you can use H2 90s and have it back for <em>Cosmo Meteor</em>
      would be right after <em>Wave Cannon</em> #1's stack resolves.</p>
      <p><b>Wave Cannon #2</b></p>
      <ul>
        <li>H2 30s, H2 120s
          <ul>
            <li>Use your mitigation when <em>Wave Cannon</em>'s cast starts.
            This will be while dodging <em>Cosmo Arrow</em> sideways to your
            spread position.</li>
            <li>H2 120s can be used slightly earlier if you want- the earliest
            would be when the first <em>Cosmo Arrow</em> lines resolve.</li>
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
      <p><em>Addle</em> will be on cooldown during this phase.</p>
      <p>It will be back up for <em>Blue Screen</em>, but there is little 
      reason to do so when mitigating <em>Run Dynamis (Delta Version)</em>
      would have greater impact.</p>
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
      <em>Run Dynamis (Omega Version)</em>, as you cannot <em>Addle</em> both 
      the <em>Solar Ray</em> before and after, <em>Run Dynamis (Omega 
      Version)</em>, but H2 can use H2 30s for the one after.</p>
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

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
