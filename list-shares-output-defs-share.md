# Untitled object in list-shares output Schema

```txt
http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [list-shares-output.json\*](samba/list-shares-output.json "open original schema") |

## share Type

`object` ([Details](list-shares-output-defs-share.md))

# share Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                 |
| :---------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                             | `string`  | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-share-name.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/name")                     |
| [description](#description)               | `string`  | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-share-description.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/description")       |
| [browseable](#browseable)                 | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-browseable.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/browseable")               |
| [enable\_recycle](#enable_recycle)        | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-enable_recycle.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_recycle")       |
| [recycle\_retention](#recycle_retention)  | `integer` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-recycle_retention.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_retention") |
| [enable\_audit](#enable_audit)            | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-enable_audit.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_audit")           |
| [log\_failed\_events](#log_failed_events) | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-log_failed_events.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/log_failed_events") |
| [acls](#acls)                             | `array`   | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-acls.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/acls")                           |

## name

Name of the share corresponding to the underlying directory name

`name`

* is optional

* Type: `string` ([Share name](list-shares-output-defs-share-properties-share-name.md))

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-share-name.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/name")

### name Type

`string` ([Share name](list-shares-output-defs-share-properties-share-name.md))

## description

Free text, known also as "comment"

`description`

* is optional

* Type: `string` ([Share description](list-shares-output-defs-share-properties-share-description.md))

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-share-description.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/description")

### description Type

`string` ([Share description](list-shares-output-defs-share-properties-share-description.md))

## browseable

If true the share is browseable to users, and is listed as a server resource. If false users must know its name to connect with it because it is not included in the network share list.

`browseable`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-browseable.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/browseable")

### browseable Type

`boolean`

## enable\_recycle

Enable the Recycle Bin for this network share.

`enable_recycle`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-enable_recycle.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_recycle")

### enable\_recycle Type

`boolean`

## recycle\_retention

Number of days deleted files are retained in the Recycle Bin before permanent removal. 0 = Infinite

`recycle_retention`

* is optional

* Type: `integer`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-recycle_retention.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_retention")

### recycle\_retention Type

`integer`

### recycle\_retention Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## enable\_audit

The basic audit log for the share is enabled

`enable_audit`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-enable_audit.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_audit")

### enable\_audit Type

`boolean`

## log\_failed\_events

Failed events are written to the audit log

`log_failed_events`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-log_failed_events.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/log_failed_events")

### log\_failed\_events Type

`boolean`

## acls



`acls`

* is optional

* Type: `object[]` ([ACL item](list-shares-output-defs-acl-item.md))

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-acls.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/acls")

### acls Type

`object[]` ([ACL item](list-shares-output-defs-acl-item.md))
