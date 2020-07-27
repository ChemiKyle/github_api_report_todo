# GitHub API Report TODO

Uses the [GitHub API](https://developer.github.com/v3/) to alert you to things that need to be done.

## Configuration

Copy `example.env` to `.env` and populate with
- **AUTH_TOKEN**: A [personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token#creating-a-token)
- **GITHUB_USERNAME**: Your GitHub username
- **ORG_NAME**: The name of an organization you're part of (currently unused)

Run the script via `python app.py` to get a (rather annoying) dialog box listing open PR reviews. The script contains some calls for assigned issues and mentions but the results still need to be parsed to condense them into something useful.

The program currently hooks into macOS notifications, but I plan to interface with other devices via [MQTT](https://en.wikipedia.org/wiki/MQTT) so please keep in mind to not couple data reception and display too tightly.
