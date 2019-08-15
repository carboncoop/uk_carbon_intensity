_Component to integrate with the [UK Carbon Intensity API][uk_carbon_intensity_api]._

## Carbon Intensity API
The [UK Carbon Intensity API][uk_carbon_intensity_api] shows the carbon intensity of the electricity on the UK grid.

## Why?
This integration may be useful to help you run home automation tasks or devices only when the grid is full of renewable energy.

**This component will set up the following platforms.**

Platform        | Description
----------------|-------------------------------------------------------
`binary_sensor` | `True` if the carbon intensity is `low` or `very low`.


## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `uk_carbon_intensity`.
4. Download _all_ the files from the `custom_components/uk_carbon_intensity/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. Choose:
   - Add `uk_carbon_intensity:` to your HA configuration.
   - In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "UK Carbon Intensity"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/uk_carbon_intensity/.translations/en.json
custom_components/uk_carbon_intensity/__init__.py
custom_components/uk_carbon_intensity/binary_sensor.py
custom_components/uk_carbon_intensity/config_flow.py
custom_components/uk_carbon_intensity/const.py
custom_components/uk_carbon_intensity/manifest.json

```

## Example configuration.yaml

```yaml
uk_carbon_intensity:

```

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

This project uses a [blueprint] for Home Assistant custom component repositories.

***
[blueprint]: https://github.com/custom-components/blueprint
[uk_carbon_intensity_api]: https://carbonintensity.org.uk/
