# Change Documentation Policy

Every Archivo 21 change begins from an identified repository or configuration
state and must remain recoverable for at least 28 days. The amount of
documentation depends on the kind of change.

## Tier D — decorative-only

A change qualifies for Tier D only when it changes visual presentation without
changing:

- wording, meaning or public claims;
- routes, destinations or navigation behaviour;
- accessibility semantics or keyboard/touch operation;
- project records, evidence, metadata or policy;
- dependencies, scripts, permissions, security controls, DNS, hosting or other
  configuration.

Tier D requires:

1. a timestamp, repository, branch/ref and exact pre-change commit;
2. a recoverable checkpoint retained for at least 28 days;
3. a concise visual scope and changed-file list;
4. focused route, responsive-navigation and accessibility regression checks;
5. the exact resulting commit and deployment result.

Tier D does not require a separate complete source ZIP, Git bundle,
file-by-file inventory, full checksum manifest or extended narrative when Git
history plus the retained checkpoint already provides complete recovery.

## Tier F — full record

Use the full documentation process for any content, functional, policy,
evidence, data, dependency, security, permissions, infrastructure,
configuration or destructive change. A mixed or ambiguous change always
defaults to Tier F.

Tier F records the exact pre-change state, relevant inventory and known
defects; preserves a complete recoverable snapshot for at least 28 days; and
documents the resulting state, differences and verification evidence.

## Classification rule

The change is classified by its highest-risk component. Calling a change
“cosmetic” or “decorative” does not make it Tier D if it alters behaviour,
meaning, accessibility or configuration.
