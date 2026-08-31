# restore-backup-content output Schema

```txt
http://schema.nethserver.org/mail/restore-backup-content-output.json
```

Extract content from a backup snapshot

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [restore-backup-content-output.json](mail/restore-backup-content-output.json "open original schema") |

## restore-backup-content output Type

`object` ([restore-backup-content output](restore-backup-content-output.md))

## restore-backup-content output Examples

```json
{
  "request": {
    "content": "Clienti/StudioV",
    "destination": "86d1a8ac-ef89-557a-8e19-8582ab86b7c4",
    "repopath": "samba/8efb6625-e70f-4a5f-9cb5-2836096d5054",
    "share": "pub",
    "snapshot": "b9ae143be9a5cf86fccff4bd7907296a3feb9f904457e3d521f215c5445cdac7"
  },
  "last_restic_message": {
    "message_type": "summary",
    "seconds_elapsed": 14,
    "total_files": 2165,
    "files_restored": 2165,
    "total_bytes": 717166163,
    "bytes_restored": 717166163
  }
}
```

# restore-backup-content output Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [request](#request)                           | `object` | Optional | cannot be null | [restore-backup-content output](restore-backup-content-output-properties-request.md "http://schema.nethserver.org/mail/restore-backup-content-output.json#/properties/request")                         |
| [last\_restic\_message](#last_restic_message) | `object` | Optional | cannot be null | [restore-backup-content output](restore-backup-content-output-properties-last_restic_message.md "http://schema.nethserver.org/mail/restore-backup-content-output.json#/properties/last_restic_message") |

## request

Original request object

`request`

* is optional

* Type: `object` ([Details](restore-backup-content-output-properties-request.md))

* cannot be null

* defined in: [restore-backup-content output](restore-backup-content-output-properties-request.md "http://schema.nethserver.org/mail/restore-backup-content-output.json#/properties/request")

### request Type

`object` ([Details](restore-backup-content-output-properties-request.md))

## last\_restic\_message

Last JSON message from Restic restore

`last_restic_message`

* is optional

* Type: `object` ([Details](restore-backup-content-output-properties-last_restic_message.md))

* cannot be null

* defined in: [restore-backup-content output](restore-backup-content-output-properties-last_restic_message.md "http://schema.nethserver.org/mail/restore-backup-content-output.json#/properties/last_restic_message")

### last\_restic\_message Type

`object` ([Details](restore-backup-content-output-properties-last_restic_message.md))
