# seek-snapshot-content output Schema

```txt
http://schema.nethserver.org/mail/seek-snapshot-content-output.json
```

Locate a file or directory in a backup snapshot

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [seek-snapshot-content-output.json](mail/seek-snapshot-content-output.json "open original schema") |

## seek-snapshot-content output Type

`object` ([seek-snapshot-content output](seek-snapshot-content-output.md))

## seek-snapshot-content output Examples

```json
{
  "request": {
    "destination": "14030a59-a4e6-54cc-b8ea-cd5f97fe44c8",
    "repopath": "mail/4372a5d5-0886-45d3-82e7-68d913716a4c",
    "snapshot": "latest",
    "share": "myshare",
    "query": "*.php",
    "limit": 100
  },
  "contents": [
    "dir1/file001.php",
    "dir1/file002.php",
    "Project/NethServer/Main.php"
  ],
  "limit_reached": false
}
```

# seek-snapshot-content output Properties

| Property                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                                   |
| :------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [contents](#contents)            | `array`   | Required | cannot be null | [seek-snapshot-content output](seek-snapshot-content-output-properties-contents.md "http://schema.nethserver.org/mail/seek-snapshot-content-output.json#/properties/contents")               |
| [limit\_reached](#limit_reached) | `boolean` | Required | cannot be null | [seek-snapshot-content output](seek-snapshot-content-output-properties-limit_reached.md "http://schema.nethserver.org/mail/seek-snapshot-content-output.json#/properties/limit_reached")     |
| [request](#request)              | `object`  | Optional | cannot be null | [seek-snapshot-content output](seek-snapshot-content-output-properties-original-request-object.md "http://schema.nethserver.org/mail/seek-snapshot-content-output.json#/properties/request") |

## contents

List of absolute share content paths

`contents`

* is required

* Type: `string[]`

* cannot be null

* defined in: [seek-snapshot-content output](seek-snapshot-content-output-properties-contents.md "http://schema.nethserver.org/mail/seek-snapshot-content-output.json#/properties/contents")

### contents Type

`string[]`

## limit\_reached

If true, the query matches more contents than the returned items

`limit_reached`

* is required

* Type: `boolean`

* cannot be null

* defined in: [seek-snapshot-content output](seek-snapshot-content-output-properties-limit_reached.md "http://schema.nethserver.org/mail/seek-snapshot-content-output.json#/properties/limit_reached")

### limit\_reached Type

`boolean`

## request



`request`

* is optional

* Type: `object` ([Original request object](seek-snapshot-content-output-properties-original-request-object.md))

* cannot be null

* defined in: [seek-snapshot-content output](seek-snapshot-content-output-properties-original-request-object.md "http://schema.nethserver.org/mail/seek-snapshot-content-output.json#/properties/request")

### request Type

`object` ([Original request object](seek-snapshot-content-output-properties-original-request-object.md))
