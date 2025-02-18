# mentation

Mentation is a Python-based utility designed to document and audit Docker environments. It provides detailed insights into Docker containers, networks, volumes, and image versions, and offers actionable recommendations to improve your Docker configurations.

## Roadmap

- List volumes, ports, networks, etc of the container.
- Identify inconsistencies in volume locations if any and provide suggestions on centralising them of not already.
- Check versions against current running version and latest and advise if out of date. link to release notes if possible.
- Based on networks, create a relationship map for containers
- Perhaps even suggest a docker compose file to recreate container if one is not present in some format