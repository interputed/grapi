class Endpoints:
    # This class contains a list of the REQUIRED keyword arguments for each API endpoint that's implemented.
    def __init__(self):
        # TODO: Allow temporarily adding new endpoints by passing in a dict.
        self._endpoints = {
            "/api/search/universal/absolute": ["query", "from", "to", "fields"],
            "/api/search/universal/absolute/terms": ["query", "from", "to", "fields"],
            "/api/search/universal/relative": ["query", "range", "fields"],
            "/api/search/universal/relative/terms": ["query", "range", "fields"]
        }

    def check(self, keys, endpoint):

        if not set(self._endpoints[endpoint]).issubset(set(keys)):
            raise ValueError("Minimum required arguments missing for this API endpoint.\n" +
                              "Given: {0}\n" +
                              "Required: {1}\n".format(args, self._endpoints))
        else:
            return True
