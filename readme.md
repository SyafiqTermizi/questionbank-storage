# Login to github docker registry

- docker login https://docker.pkg.github.com -u syafiqtermizi
- password is your PAT https://github.com/settings/tokens

# Build docker image

docker build -t docker.pkg.github.com/syafiqtermizi/questionbank-storage/qbankstorage:latest -f docker/prod.Dockerfile .

# Push docker image to github docker registry

docker push docker.pkg.github.com/syafiqtermizi/questionbank-storage/qbankstorage:latest
