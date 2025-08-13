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
    <td>Sunburst Holy x4</td>
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
        <li>ST Reprisal, H2 30s, D2</li>
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
        <li>MT + ST Rampant + 40% + 3rd + short.</li>
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
        <li>H2 30s, D1</li>
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
- The default plan below has five party mitigations for *Hallowed Wings*, which
  is overkill and leaves a weak spot at *Memory's End* and *Morn Afah* #1.
  Consider moving one tank's 90s party mitigation (especially if they are
  WAR/PLD) forward to cover *Memory's End* → *Morn Afah* #1 instead of 
  *Darklit Dragonsong* → *Hallowed Wings*.

<table>
  <tr>
    <td>
      <p>Darklit Dragonsong</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, MT 90s, ST 90s, D2, D3</li>
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
    </td>
    <td>
      <ul>
        <li>Covered by ST <em>Reprisal</em> and H2 30s from <em>Akh Morn</em>.</li>
        <li>Debuffs should target the <em>Usurper of Frost</em>.</li>
        <li>Use any extra mitigation here.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Crystallize Time</p>
    </td>
    <td>
      <ul>
        <li>MT Reprisal, D1, D4</li>
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

The default mitigation plan has *both* tanks use their 90s party mitigation at
*Hallowed Wings* during *Crystallize Time*. However, this is too much 
mitigation at this spot (MT 90s, ST 90s, H1 120s, H2 120s, D3), which leaves a
bit of a weak spot at *Memory's End* and *Morn Afah* #1.

Consider having one tank (especially if they are WAR/PLD) move their 90s party
mitigation from *Darklit Dragonsong* → *Hallowed Wings* to *Memory's End* → 
*Morn Afah* #1.

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
      <p><b>Fire/Unholy Darkness #2 or #3</b></p>
      <ul>
        <li>MT 90s</li>
      </ul>
      <p>Feel free to use <em>Reprisal</em> anywhere else in this phase
      <em>before</em> the final <em>Dark Water III</em> stacks at
      <em>Apocalypse</em>.</p>
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
      <p><b>Crystallize Time (Hallowed Wings)</b></p>
      <ul>
        <li>MT 90s, 40%
          <ul>
            <li>Use these around the time the Oracle of Darkness jumps on
            someone (<em>Spirit Taker</em>) just before the rewind resolves.</li>
            <li>The party actually has more than enough mitigation for
            <em>Hallowed Wings</em>. Consider having one tank move their 90s 
            forward to cover <em>Morn Afah</em> #1 instead, especially if they 
            are WAR/PLD. That tank should also bring their 90s mitigations 
            forward to <em>Memory's End</em> and <em>Morn Afah</em> #1.</li>
          </ul>
        </li>
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

The default mitigation plan has *both* tanks use their 90s party mitigation at
*Hallowed Wings* during *Crystallize Time*. However, this is too much 
mitigation at this spot (MT 90s, ST 90s, H1 120s, H2 120s, D3), which leaves a
bit of a weak spot at *Memory's End* and *Morn Afah* #1.

Consider having one tank (especially if they are WAR/PLD) move their 90s party
mitigation from *Darklit Dragonsong* → *Hallowed Wings* to *Memory's End* → 
*Morn Afah* #1.

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
      <p><b>Shell Crusher → Shockwave Pulsar #1</b></p>
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
      <p><b>Akh Morn → Morn Afah #1</b></p>
      <ul>
        <li><em>Reprisal</em></li>
      </ul>
      <p><b>Crystallize Time (Hallowed Wings)</b></p>
      <ul>
        <li>ST 90s, 40%
          <ul>
            <li>Use this around the time the Oracle of Darkness jumps on
            someone (<em>Spirit Taker</em>) just before the rewind resolves.</li>
            <li>The party actually has more than enough mitigation for
            <em>Hallowed Wings</em>. Consider having one tank move their 90s 
            forward to cover <em>Morn Afah</em> #1 instead, especially if they 
            are WAR/PLD. That tank should also bring their 90s mitigations 
            forward to <em>Memory's End</em> and <em>Morn Afah</em> #1.</li>
          </ul>
        </li>
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
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Burnished Glory #1</b></p>
      <ul>
        <li>H1 120s
          <ul>
            <li>Use your 120s mitigation early (when the knockback happens just
            before the boss reappears). You only need to cover the initial damage
            from <em>Burnished Glory</em>.</li>
            <li>Use your 180s abilities early as well, if you want to use them
            again at <em>Mirror, Mirror</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Sunburst Holy</b></p>
      <ul>
        <li>H1 120s</li>
      </ul>
      <p><b>Absolute Zero</b></p>
      <ul>
        <li>H1 120s</li>
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
        <li>H1 120s
          <ul>
            <li>This may seem strange, but it's used early here to be back in
            time for the final <em>Shockwave Pulsar</em> → <em>Memory's End</em>
            sequence, and should also cover the first set of <em>Dark Fire
            III</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Shockwave Pulsar #2</b></p>
      <ul>
        <li>H1 120s</li>
        <ul>
          <li>Use this a bit before the cast resolves to cover <em>Memory's
          End</em> as well.</li>
        </ul>
      </ul>
      <p><b>Memory's End</b></p>
      <ul>
        <li>H1 120s</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Gaia and Shiva</b></p>
    </td>
    <td>
      <p><b>Crystallize Time</b></p>
      <ul>
        <li>H1 120s
          <ul>
            <li>You can use this when the <em>Spell in Waiting: Quietus</em>
            resolves, and it will still cover the <em>Hallowed Wings</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Pandora</b></p>
    </td>
    <td>
      <p><b>Polarising Strikes #1</b></p>
      <ul>
        <li>H1 120s</li>
        <ul>
          <li>Use this no earlier than when the cast bar reaches the "P" in
          <em>Polarizing Strikes</em> to cover all four hits.</li>
        </ul>
      </ul>
      <p><b>Polarising Strikes #2</b></p>
      <ul>
        <li>H1 180s</li>
      </ul>
      <p><b>Fulgent Blade #3</b></p>
      <ul>
        <li>H1 120s</li>
        <ul>
          <li>This <em>cannot</em> cover both <em>Fulgent Blade</em> and
          <em>Akh Morn</em>.</li>
        </ul>
      </ul>
    </td>
  </tr>
</table>

### H2

<table>
  <tr>
    <td>
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Cyclonic Break</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>Use this no earlier than when the cast-bar reaches the "C" in
            <em>Cyclonic Break</em> to also help the MT for <em>Powder Mark
            Trail</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Burnished Glory #1</b></p>
      <ul>
        <li>H2 30s, H2 120s
          <ul>
            <li>Use your 120s mitigation early (when the knockback happens just
            before the boss reappears). You only need to cover the initial damage
            from <em>Burnished Glory</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Burnished Glory #2</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>Use this after the second tether resolves in <em>Fall of
            Faith</em> to cover the last two tethers and the initial hit from
            <em>Burnished Glory</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Diamond Dust</b></p>
      <ul>
        <li>H2 30s, H2 120s</li>
      </ul>
      <p><b>Hallowed Ray</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Light Rampant</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>House of Light</b></p>
      <ul>
        <li>H2 120s
          <ul>
            <li>Use this early to also cover the <em>Banish III</em> stacks at
            the end of <em>Light Rampant</em> in addition to <em>House of
            Light</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Absolute Zero</b></p>
      <ul>
        <li>H2 30s</li>
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
        <li>H2 120s
          <ul>
            <li>This may seem strange, but it's used early here to be back in
            time for the final <em>Shockwave Pulsar</em> → <em>Memory's End</em>
            sequence, and should also cover the first set of <em>Dark Fire
            III</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Spell in Waiting: Dark Fire III #1</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Shockwave Pulsar #1</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Apocalypse (Spell in Waiting: Dark Water III #1)</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Shockwave Pulsar #2</b></p>
      <ul>
        <li>H2 120s</li>
        <ul>
          <li>Use this a bit before the cast resolves to cover <em>Memory's
          End</em> as well.</li>
        </ul>
      </ul>
      <p><b>Memory's End</b></p>
      <ul>
        <li>H2 30s, H2 120s</li>
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
        <li>H2 30s</li>
      </ul>
      <p><b>Akh Morn → Morn Afah #1</b></p>
      <ul>
        <li>H2 30s
          <ul>
            <li>If you use this when the Oracle of Darkness jumps for the
            second time for <em>Somber Dance</em>, it will cover the four
            <em>Akh Morn</em> hits, and be back in time for the start of
            <em>Crystallize Time</em>. However, it will <em>not</em> cover
            <em>Morn Afah</em> if you do so.</li>
          </ul>
        </li>
      </ul>
      <p><b>Crystallize Time</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
      <p><b>Crystallize Time (Hallowed Wings)</b></p>
      <ul>
        <li>H2 120s
          <ul>
            <li>You can use this when the <em>Spell in Waiting: Quietus</em>
            resolves, and it will still cover the <em>Hallowed Wings</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Akh Morn → Morn Afah #2</b></p>
      <ul>
        <li>H2 30s</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Pandora</b></p>
    </td>
    <td>
      <p><b>Polarising Strikes #1</b></p>
      <ul>
        <li>H2 120s</li>
        <ul>
          <li>Use this no earlier than when the cast bar reaches the "P" in
          <em>Polarizing Strikes</em> to cover all four hits.</li>
        </ul>
      </ul>
      <p><b>Polarising Strikes #2</b></p>
      <ul>
        <li>H2 180s</li>
      </ul>
      <p><b>Fulgent Blade #3</b></p>
      <ul>
        <li>H2 120s</li>
        <ul>
          <li>This <em>cannot</em> cover both <em>Fulgent Blade</em> and
          <em>Akh Morn</em>.</li>
        </ul>
      </ul>
    </td>
  </tr>
</table>

### D1

<table>
  <tr>
    <td>
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Cyclonic Break</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>Use this no earlier than when the cast-bar reaches the "C" in
            <em>Cyclonic Break</em> to also help the MT for <em>Powder Mark
            Trail</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Burnished Glory #2</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>Use this after the second tether resolves in <em>Fall of
            Faith</em> to cover the last two tethers and the initial hit from
            <em>Burnished Glory</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Hallowed Ray</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Absolute Zero</b></p>
      <ul>
        <li><em>Feint</em></li>
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
        <li><em>Feint</em></li>
      </ul>
      <p><b>Memory's End</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Gaia and Shiva</b></p>
    </td>
    <td>
      <p><b>Crystallize Time</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>Make sure you <em>Feint</em> the Oracle of Darkness.</li>
          </ul>
        </li>
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
        <li><em>Feint</em></li>
      </ul>
      <p><b>Fulgent Blade #2</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>Use this when the castbar reaches the "B" in <em>Pandora's
            Box</em> to cover <em>Pandora's Box</em> in addition to <em>Fulgent
            Blade</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Fulgent Blade #3</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
</table>

### D2

This assumes D2 is a melee DPS.

<table>
  <tr>
    <td>
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Burnished Glory #1</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Diamond Dust</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Light Rampant</b></p>
      <ul>
        <li><em>Feint</em>
          <ul>
            <li>You can use this early to also cover the <em>Banish III</em>
            stacks at the end of <em>Mirror, Mirror</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Oracle of Darkness</b></p>
    </td>
    <td>
      <p><b>Shell Crusher → Shockwave Pulsar #1</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Memory's End</b></p>
      <ul>
        <li><em>Feint</em></li>
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
        <li><em>Feint</em>
          <ul>
            <li>Make sure you <em>Feint</em> the Usurper of Frost.</li>
          </ul>
        </li>
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
        <li><em>Feint</em></li>
      </ul>
      <p><b>Akh Morn #2</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
      <p><b>Akh Morn #3</b></p>
      <ul>
        <li><em>Feint</em></li>
      </ul>
    </td>
  </tr>
</table>

### D3

<table>
  <tr>
    <td>
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Cyclonic Break</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>Use this no earlier than when the cast-bar reaches the "C" in
            <em>Cyclonic Break</em> to also help the MT for <em>Powder Mark
            Trail</em>.</li>
          </ul>
        </li>
      </ul>
      <p><b>Burnished Glory #2</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>Use this after the second tether resolves in <em>Fall of
            Faith</em> to cover the last two tethers and the initial hit from
            <em>Burnished Glory</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Sunburst Holy</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>Use this no earlier than when the star AoE puddles are dropped at
            the start of <em>Diamond Dust</em> to cover all four <em>Sunburst
            Holy</em> stacks.</li>
          </ul>
        </li>
      </ul>
      <p><b>Absolute Zero</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Oracle of Darkness</b></p>
    </td>
    <td>
      <p><b>Spell in Waiting: Fire III #2 or #3</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
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
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
      <p><b>Crystallize Time (Hallowed Wings)</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em>
          <ul>
            <li>Use this around the time the Oracle of Darkness jumps on
            someone (<em>Spirit Taker</em>) just before the rewind
            resolves.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P5. Pandora</b></p>
    </td>
    <td>
      <p><b>Polarizing Strikes #1</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
      <p><b>Polarizing Strikes #2</b></p>
      <ul>
        <li><em>Troubadour/Tactician/Shield Samba</em></li>
      </ul>
    </td>
  </tr>
</table>

### D4

<table>
  <tr>
    <td>
      <p><b>P1. Fatebreaker</b></p>
    </td>
    <td>
      <p><b>Burnished Glory #1</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P2. Usurper of Frost</b></p>
    </td>
    <td>
      <p><b>Diamond Dust</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p><b>Light Rampant</b></p>
      <ul>
        <li><em>Addle</em>
          <ul>
            <li>You can use this early to also cover the <em>Banish III</em>
            stacks at the end of <em>Mirror, Mirror</em>.</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P3. Oracle of Darkness</b></p>
    </td>
    <td>
      <p><b>Shell Crusher → Shockwave Pulsar #1</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p><b>Memory's End</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p><b>P4. Gaia and Shiva</b></p>
    </td>
    <td>
      <p><b>Crystallize Time</b></p>
      <ul>
        <li><em>Addle</em>
          <ul>
            <li>Make sure you <em>Addle</em> the Oracle of Darkness.</li>
          </ul>
        </li>
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
        <li><em>Addle</em></li>
      </ul>
      <p><b>Akh Morn #2</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
      <p><b>Akh Morn #3</b></p>
      <ul>
        <li><em>Addle</em></li>
      </ul>
    </td>
  </tr>
</table>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
