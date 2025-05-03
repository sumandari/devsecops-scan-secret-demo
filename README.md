# Sometimes you accidentally push your secret :(

- This is a demo to show that someone could accidentally push a secret and forgot that it is in the commit history.

- We will use [gitleaks docker image](https://hub.docker.com/r/zricethezav/gitleaks) for this demo.

```bash
export path_to_host_folder_to_scan=.
docker pull zricethezav/gitleaks:latest
docker run -v ${path_to_host_folder_to_scan}:/path zricethezav/gitleaks:latest detect --source="/path" --verbose
```