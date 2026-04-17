# Acceptance Review Checklist

## Proposal: P-YYYYMMDD-XXX - <Title>

**Review Date**: YYYY-MM-DD
**Reviewer**: 小墨
**Status**: `in_acceptance`

---

## 1. Requirements Consistency

- [ ] Matches requester-confirmed requirements
- [ ] Aligns with PRD
- [ ] No scope creep or shortcuts
- [ ] All acceptance criteria met

## 2. Functional Verification

- [ ] Core functionality works end-to-end
- [ ] No errors in console/logs (warnings OK)
- [ ] Existing functionality not broken
- [ ] Build succeeds (`npm run build` / `cargo build` / `go build` / etc.)

## 3. Delivery Completeness

- [ ] File paths provided
- [ ] Startup/access instructions provided
- [ ] Verification results or screenshots provided

## 4. Quality Check

- [ ] No obvious gaps
- [ ] No UI/logic conflicts
- [ ] Known limitations documented
- [ ] Code is maintainable

## 5. Dev Delivery Quality Checks (Hard Indicators)

| Check | Result |
|-------|--------|
| Build exit code = 0 | ⬜ |
| Output directory not empty | ⬜ |
| Core source/service files exist | ⬜ |

## 6. Verification Evidence

**Build Output:**
```
(paste build output here)
```

**Core Files List:**
```
(list core files here)
```

**Verification Notes:**
-

---

## Final Verdict

- [ ] **ACCEPTED** - All checks passed
- [ ] **NEEDS REVISION** - Issues found (see below)

## Revision Notes

- **Issue**: <description>
- **Impact**: <what is affected>
- **Expected fix**: <how to fix and how to verify>

