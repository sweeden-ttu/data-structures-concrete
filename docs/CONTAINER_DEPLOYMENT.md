# Container Deployment

## Development Container with Podman

### Build Image

```bash
podman build -t data-structures-concrete-dev .
```

### Run Tests in Container

```bash
podman run --rm -it \
  -v $(pwd):/workspace \
  data-structures-concrete-dev \
  pytest src/python/
```

### Interactive Development

```bash
podman run --rm -it \
  -v $(pwd):/workspace \
  -w /workspace \
  data-structures-concrete-dev \
  bash
```

## Docker Compose for Integration Testing

```yaml
version: '3.8'
services:
  test:
    build: .
    volumes:
      - .:/workspace
    command: pytest src/python/ -v
```

## CI/CD Usage

```bash
podman build -t data-structures-concrete-test -f Containerfile.ci .
podman run --rm data-structures-concrete-test pytest
```
