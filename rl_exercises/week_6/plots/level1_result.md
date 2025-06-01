# Level 1

4. Analyze the results:
   - Do some baselines learn faster or reach higher returns?
          - During the first 40000 steps `none` and `avg` learn faster than `value` and `gae`.
          - Though afterwards all baselines result in similiar learning-speeds and return values.

   - Provide a conceptual justification for any observed differences (e.g. variance reduction, bias–variance trade‑off).
          - from lecture: "value baselines + GAE give a low-variance direction but can still produce oversized steps after lucky trajectories."
          - `value` and `gae` seem to produce these oversized steps each one time in the first 40000 steps