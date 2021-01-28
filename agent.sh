# be sure to choose an environment (dev, staging, prod)
prefect agent docker start --token $PREFECT_PROD_RUNNER_TOKEN --label production

# ~/d/pgr_examples_2> prefect agent docker start -h 
# Usage: prefect agent docker start [OPTIONS]

#   Start a docker agent

# Options:
#   -t, --token TEXT                A Prefect Cloud API token with RUNNER scope.
#   -a, --api TEXT                  A Prefect API URL.
#   --agent-config-id TEXT          An agent ID to link this agent instance with
#   -n, --name TEXT                 A name to use for the agent
#   -l, --label TEXT                Labels the agent will use to query for flow
#                                   runs.

#   -e, --env TEXT                  Environment variables to set on each
#                                   submitted flow run.

#   --max-polls INTEGER             Maximum number of times the agent should
#                                   poll the Prefect API for flow runs. Default
#                                   is no limit

#   --agent-address TEXT            Address to serve internal api server at.
#                                   Defaults to no server.

#   --no-cloud-logs                 Turn off logging for all flows run through
#                                   this agent.

#   --log-level [DEBUG|INFO|WARNING|ERROR]
#                                   The agent log level to use. Defaults to the
#                                   value configured in your environment.

#   -b, --base-url TEXT             Docker daemon base URL.
#   --no-pull                       Disable pulling images in the agent
#   -f, --show-flow-logs            Display logging output from flows run by the
#                                   agent.

#   --volume TEXT                   Host paths for Docker bind mount volumes
#                                   attached to each Flow container. Can be
#                                   provided multiple times to pass multiple
#                                   volumes (e.g. `--volume /volume1 --volume
#                                   /volume2`)

#   --network TEXT                  Add containers to an existing docker network
#   --no-docker-interface           Disable the check of a Docker interface on
#                                   this machine. Note: This is mostly relevant
#                                   for some Docker-in-Docker setups that users
#                                   may be running their agent with.

#   -h, --help                      Show this message and exit.