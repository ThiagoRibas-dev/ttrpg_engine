# AI Designer — 0750

Confirmed both points:

1. **Rewrite, not move.** Migration = extract rules from the archived snapshot, write one clean canonical specification per owner (regrouped by owner, restructured per the spec template, interlinked per DEC-104), register the node/edges in the YAML registry, add a manifest row, and list open definitions. The archive stays untouched as the historical record. Content-fidelity boundary restated: migration must not silently change rule meaning — approved wording changes (e.g. DEC-102 deprecations) apply during rewrite, but any substantive rule change requires a new DEC or an explicitly listed open definition.

2. **Hybrid: Markdown links + inline-HTML anchors.** Links use standard Markdown `[Label](path#anchor)`; stable anchors use inline HTML `<a id="..."></a>` inside headings, per DEC-104 (e.g. `## Stamina <a id="resource-stamina"></a>`), because auto-generated heading slugs change when heading text changes. Noted that the sandboxed workspace preview may not render the HTML anchor tags, which is precisely why validating the anchor syntax in the user's real target renderer is queued as next step 1 (reorg model §15.5), with fallbacks (auto-slugs or `{#id}` extensions) if HTML is sanitized.
