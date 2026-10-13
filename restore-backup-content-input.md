# restore-backup-content input Schema

```txt
http://schema.nethserver.org/mail/restore-backup-content-input.json
```

Extract content from a backup snapshot

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [restore-backup-content-input.json](mail/restore-backup-content-input.json "open original schema") |

## restore-backup-content input Type

`object` ([restore-backup-content input](restore-backup-content-input.md))

## restore-backup-content input Examples

```json
{
  "snapshot": "b9ae143be9a5cf86fccff4bd7907296a3feb9f904457e3d521f215c5445cdac7",
  "destination": "86d1a8ac-ef89-557a-8e19-8582ab86b7c4",
  "repopath": "samba/8efb6625-e70f-4a5f-9cb5-2836096d5054",
  "share": "pub",
  "content": "Clienti/StudioV"
}
```

# restore-backup-content input Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                           |
| :-------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [destination](#destination) | `string` | Required | cannot be null | [restore-backup-content input](restore-backup-content-input-properties-destination.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/destination") |
| [repopath](#repopath)       | `string` | Required | cannot be null | [restore-backup-content input](restore-backup-content-input-properties-repopath.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/repopath")       |
| [snapshot](#snapshot)       | `string` | Required | cannot be null | [restore-backup-content input](restore-backup-content-input-properties-snapshot.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/snapshot")       |
| [share](#share)             | `string` | Required | cannot be null | [restore-backup-content input](restore-backup-content-input-properties-share.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/share")             |
| [destroot](#destroot)       | `string` | Optional | cannot be null | [restore-backup-content input](restore-backup-content-input-properties-destroot.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/destroot")       |
| [content](#content)         | `string` | Required | cannot be null | [restore-backup-content input](restore-backup-content-input-properties-content.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/content")         |

## destination

The UUID of the backup destination where the Restic repository resides.

`destination`

* is required

* Type: `string`

* cannot be null

* defined in: [restore-backup-content input](restore-backup-content-input-properties-destination.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/destination")

### destination Type

`string`

## repopath

Restic repository path, under the backup destination

`repopath`

* is required

* Type: `string`

* cannot be null

* defined in: [restore-backup-content input](restore-backup-content-input-properties-repopath.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/repopath")

### repopath Type

`string`

## snapshot

Restic snapshot ID to restore

`snapshot`

* is required

* Type: `string`

* cannot be null

* defined in: [restore-backup-content input](restore-backup-content-input-properties-snapshot.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/snapshot")

### snapshot Type

`string`

## share

Seek the paths of this Samba share

`share`

* is required

* Type: `string`

* cannot be null

* defined in: [restore-backup-content input](restore-backup-content-input-properties-share.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/share")

### share Type

`string`

### share Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")

## destroot

Name of a share root-level directory where content is restored. Existing content is removed before restoring the backup.

`destroot`

* is optional

* Type: `string`

* cannot be null

* defined in: [restore-backup-content input](restore-backup-content-input-properties-destroot.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/destroot")

### destroot Type

`string`

### destroot Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")

## content

Content path to restore

`content`

* is required

* Type: `string`

* cannot be null

* defined in: [restore-backup-content input](restore-backup-content-input-properties-content.md "http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/content")

### content Type

`string`
