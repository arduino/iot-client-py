# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.api.things_v2_api import ThingsV2Api


class TestThingsV2Api(unittest.TestCase):
    """ThingsV2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = ThingsV2Api()

    def tearDown(self) -> None:
        pass

    def test_things_v2_clone(self) -> None:
        """Test case for things_v2_clone

        clone things_v2
        """
        pass

    def test_things_v2_create(self) -> None:
        """Test case for things_v2_create

        create things_v2
        """
        pass

    def test_things_v2_create_sketch(self) -> None:
        """Test case for things_v2_create_sketch

        createSketch things_v2
        """
        pass

    def test_things_v2_delete(self) -> None:
        """Test case for things_v2_delete

        delete things_v2
        """
        pass

    def test_things_v2_delete_sketch(self) -> None:
        """Test case for things_v2_delete_sketch

        deleteSketch things_v2
        """
        pass

    def test_things_v2_list(self) -> None:
        """Test case for things_v2_list

        list things_v2
        """
        pass

    def test_things_v2_show(self) -> None:
        """Test case for things_v2_show

        show things_v2
        """
        pass

    def test_things_v2_template(self) -> None:
        """Test case for things_v2_template

        template things_v2
        """
        pass

    def test_things_v2_update(self) -> None:
        """Test case for things_v2_update

        update things_v2
        """
        pass

    def test_things_v2_update_sketch(self) -> None:
        """Test case for things_v2_update_sketch

        updateSketch things_v2
        """
        pass


if __name__ == '__main__':
    unittest.main()
