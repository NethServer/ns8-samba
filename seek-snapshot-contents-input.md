# seek-snapshot-contents input Schema

```txt
http://schema.nethserver.org/mail/seek-snapshot-contents-input.json
```

Locate a file or directory in a backup snapshot

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [seek-snapshot-contents-input.json](mail/seek-snapshot-contents-input.json "open original schema") |

## seek-snapshot-contents input Type

`object` ([seek-snapshot-contents input](seek-snapshot-contents-input.md))

## seek-snapshot-contents input Examples

```json
{
  "snapshot": "b9ae143be9a5cf86fccff4bd7907296a3feb9f904457e3d521f215c5445cdac7",
  "destination": "86d1a8ac-ef89-557a-8e19-8582ab86b7c4",
  "repopath": "samba/8efb6625-e70f-4a5f-9cb5-2836096d5054",
  "share": "Complex Shar€ name"
}
```

```json
{
  "snapshot": "b9ae143be9a5cf86fccff4bd7907296a3feb9f904457e3d521f215c5445cdac7",
  "destination": "86d1a8ac-ef89-557a-8e19-8582ab86b7c4",
  "repopath": "samba/8efb6625-e70f-4a5f-9cb5-2836096d5054",
  "share": "Complex Shar€ name",
  "limit": 50,
  "query": "MYFILE.TXT"
}
```

# seek-snapshot-contents input Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                           |
| :-------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [destination](#destination) | `string`  | Required | cannot be null | [seek-snapshot-contents input](seek-snapshot-contents-input-properties-destination.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/destination") |
| [repopath](#repopath)       | `string`  | Required | cannot be null | [seek-snapshot-contents input](seek-snapshot-contents-input-properties-repopath.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/repopath")       |
| [snapshot](#snapshot)       | `string`  | Required | cannot be null | [seek-snapshot-contents input](seek-snapshot-contents-input-properties-snapshot.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/snapshot")       |
| [share](#share)             | `string`  | Required | cannot be null | [seek-snapshot-contents input](seek-snapshot-contents-input-properties-share.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/share")             |
| [query](#query)             | `string`  | Optional | cannot be null | [seek-snapshot-contents input](seek-snapshot-contents-input-properties-query.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/query")             |
| [limit](#limit)             | `integer` | Optional | cannot be null | [seek-snapshot-contents input](seek-snapshot-contents-input-properties-limit.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/limit")             |

## destination

The UUID of the backup destination where the Restic repository resides.

`destination`

* is required

* Type: `string`

* cannot be null

* defined in: [seek-snapshot-contents input](seek-snapshot-contents-input-properties-destination.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/destination")

### destination Type

`string`

## repopath

Restic repository path, under the backup destination

`repopath`

* is required

* Type: `string`

* cannot be null

* defined in: [seek-snapshot-contents input](seek-snapshot-contents-input-properties-repopath.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/repopath")

### repopath Type

`string`

## snapshot

Restic snapshot ID to restore

`snapshot`

* is required

* Type: `string`

* cannot be null

* defined in: [seek-snapshot-contents input](seek-snapshot-contents-input-properties-snapshot.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/snapshot")

### snapshot Type

`string`

## share

Seek the paths of this Samba share

`share`

* is required

* Type: `string`

* cannot be null

* defined in: [seek-snapshot-contents input](seek-snapshot-contents-input-properties-share.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/share")

### share Type

`string`

### share Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")

## query

Seek matching paths

`query`

* is optional

* Type: `string`

* cannot be null

* defined in: [seek-snapshot-contents input](seek-snapshot-contents-input-properties-query.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/query")

### query Type

`string`

## limit

Limit the number of returned contents

`limit`

* is optional

* Type: `integer`

* cannot be null

* defined in: [seek-snapshot-contents input](seek-snapshot-contents-input-properties-limit.md "http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/limit")

### limit Type

`integer`
