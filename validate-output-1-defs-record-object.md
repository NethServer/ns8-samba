# Untitled object in export-users output Schema

```txt
http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [validate-output.json\*](export-users/validate-output.json "open original schema") |

## record-object Type

`object` ([Details](validate-output-1-defs-record-object.md))

# record-object Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                              |
| :-------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [user](#user)                                       | `string`  | Required | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-user.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/user")                                     |
| [display\_name](#display_name)                      | `string`  | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-display_name.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/display_name")                     |
| [locked](#locked)                                   | `boolean` | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-locked.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/locked")                                 |
| [groups](#groups)                                   | `array`   | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-groups.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/groups")                                 |
| [mail](#mail)                                       | `string`  | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-email-address.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/mail")                            |
| [must\_change\_password](#must_change_password)     | `boolean` | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-must_change_password.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/must_change_password")     |
| [no\_password\_expiration](#no_password_expiration) | `boolean` | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-no_password_expiration.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/no_password_expiration") |

## user



`user`

* is required

* Type: `string`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-user.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/user")

### user Type

`string`

## display\_name



`display_name`

* is optional

* Type: `string`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-display_name.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/display_name")

### display\_name Type

`string`

## locked

If true, the account is locked, preventing logins

`locked`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-locked.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/locked")

### locked Type

`boolean`

### locked Default Value

The default value is:

```json
false
```

## groups

List of groups

`groups`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-groups.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/groups")

### groups Type

`string[]`

## mail



`mail`

* is optional

* Type: `string` ([Email address](validate-output-1-defs-record-object-properties-email-address.md))

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-email-address.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/mail")

### mail Type

`string` ([Email address](validate-output-1-defs-record-object-properties-email-address.md))

## must\_change\_password

If true, the user must change their password at next login

`must_change_password`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-must_change_password.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/must_change_password")

### must\_change\_password Type

`boolean`

## no\_password\_expiration

If true, the user's password will not expire

`no_password_expiration`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-no_password_expiration.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/no_password_expiration")

### no\_password\_expiration Type

`boolean`
