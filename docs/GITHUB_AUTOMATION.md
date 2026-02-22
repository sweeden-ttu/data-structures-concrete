# GitHub Automation

## Daily Sync Script

Run `scripts/daily-github-sync.sh` to sync with remote repositories.

## Automation Features

- Automatic fetch and rebase
- Branch synchronization
- Commit status checks

## Cron Setup

```bash
0 6 * * * /path/to/projects/data-structures-concrete/scripts/daily-github-sync.sh >> /var/log/github-sync.log 2>&1
```

## GitHub Actions

Workflows are defined in `.github/workflows/`:

- `test.yml` - Run tests on push/PR
- `lint.yml` - Code quality checks
- `benchmark.yml` - Performance benchmarks

## Release Process

1. Create release branch
2. Update version in `__init__.py`
3. Create GitHub release
4. Publish to PyPI (if applicable)
