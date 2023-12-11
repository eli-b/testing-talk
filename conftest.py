from hypothesis import settings, HealthCheck

# Create a hypothesis profile which allows using function-scoped fixures in test functions wrapped by hypothesis.given:
# (See https://hypothesis.readthedocs.io/en/latest/settings.html#hypothesis.HealthCheck.function_scoped_fixture)
settings.register_profile(
    "suppress",
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
