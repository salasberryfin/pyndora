class ClientAssetRecord:

    def from_json(asset):
        """
        Builds a client record from a JSON-encoded asset record.

        Parameters
            asset:json dict     json-encoded asset record.

        """

        # TODO
        # have no idea what this actually does
        return asset

    def to_json():

        # TODO
        pass


class OwnerMemo:

    def from_json():

        # TODO
        pass


def open_client_asset_record(asset_record, owner_memo, keypair):
    """
    Create JSON object with relevant information about
    the given asset record.

    **Default asset type to FRA asset code -> validate how
    to retrieve actual asset code.
    """

    if owner_memo:
        print("do stuff")

    record = asset_record["record"]
    asset_data = {
        "blind_asset_record": record,
        "amount": record["amount"]["NonConfidential"],
        "amount_blinds": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        "asset_type": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
    }

    return asset_data
