# alter-user input Schema

```txt
http://schema.nethserver.org/samba/alter-user-input.json
```

Alter an existing user. Only the user identifier attibute is mandatory

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [alter-user-input.json](samba/alter-user-input.json "open original schema") |

## alter-user input Type

`object` ([alter-user input](alter-user-input.md))

## alter-user input Examples

```json
{
  "user": "alice",
  "display_name": "Alice Jordan",
  "password": "secret",
  "locked": false,
  "groups": [
    "developers",
    "managers"
  ],
  "mail": "alice@nethserver.org",
  "must_change_password": true,
  "no_password_expiration": false
}
```

# alter-user input Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                              |
| :-------------------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [user](#user)                                       | `string`  | Required | cannot be null | [alter-user input](alter-user-input-properties-user-identifier.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/user")                          |
| [display\_name](#display_name)                      | `string`  | Optional | cannot be null | [alter-user input](alter-user-input-properties-display-name.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/display_name")                     |
| [password](#password)                               | `string`  | Optional | cannot be null | [alter-user input](alter-user-input-properties-new-password.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/password")                         |
| [locked](#locked)                                   | `boolean` | Optional | cannot be null | [alter-user input](alter-user-input-properties-locked.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/locked")                                 |
| [groups](#groups)                                   | `array`   | Optional | cannot be null | [alter-user input](alter-user-input-properties-group-membership.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/groups")                       |
| [mail](#mail)                                       | Merged    | Optional | cannot be null | [alter-user input](alter-user-input-properties-email-address.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/mail")                            |
| [must\_change\_password](#must_change_password)     | `boolean` | Optional | cannot be null | [alter-user input](alter-user-input-properties-must-change-password.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/must_change_password")     |
| [no\_password\_expiration](#no_password_expiration) | `boolean` | Optional | cannot be null | [alter-user input](alter-user-input-properties-no-password-expiration.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/no_password_expiration") |

## user

The user must exist

`user`

* is required

* Type: `string` ([User identifier](alter-user-input-properties-user-identifier.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-user-identifier.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/user")

### user Type

`string` ([User identifier](alter-user-input-properties-user-identifier.md))

### user Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## display\_name



`display_name`

* is optional

* Type: `string` ([Display name](alter-user-input-properties-display-name.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-display-name.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/display_name")

### display\_name Type

`string` ([Display name](alter-user-input-properties-display-name.md))

### display\_name Constraints

**maximum length**: the maximum number of characters for this string is: `32`

## password

If empty, a random password is set

`password`

* is optional

* Type: `string` ([New password](alter-user-input-properties-new-password.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-new-password.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/password")

### password Type

`string` ([New password](alter-user-input-properties-new-password.md))

### password Constraints

**minimum length**: the minimum number of characters for this string is: `0`

## locked

True, if the user account has been locked, preventing the user from logging in

`locked`

* is optional

* Type: `boolean` ([Locked](alter-user-input-properties-locked.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-locked.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/locked")

### locked Type

`boolean` ([Locked](alter-user-input-properties-locked.md))

## groups

Set the user as a member of the given list of groups

`groups`

* is optional

* Type: `string[]` ([Group identifier](alter-user-input-properties-group-membership-group-identifier.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-group-membership.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/groups")

### groups Type

`string[]` ([Group identifier](alter-user-input-properties-group-membership-group-identifier.md))

## mail



`mail`

* is optional

* Type: `string` ([Email address](alter-user-input-properties-email-address.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-email-address.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/mail")

### mail Type

`string` ([Email address](alter-user-input-properties-email-address.md))

one (and only one) of

* [Untitled string in alter-user input](alter-user-input-properties-email-address-oneof-0.md "check type definition")

* [Untitled string in alter-user input](alter-user-input-properties-email-address-oneof-1.md "check type definition")

## must\_change\_password

If true, the user must change their password at next login

`must_change_password`

* is optional

* Type: `boolean` ([Must change password](alter-user-input-properties-must-change-password.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-must-change-password.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/must_change_password")

### must\_change\_password Type

`boolean` ([Must change password](alter-user-input-properties-must-change-password.md))

## no\_password\_expiration

If true, the user's password will not expire. If false, the domain policy is applied

`no_password_expiration`

* is optional

* Type: `boolean` ([No password expiration](alter-user-input-properties-no-password-expiration.md))

* cannot be null

* defined in: [alter-user input](alter-user-input-properties-no-password-expiration.md "http://schema.nethserver.org/samba/alter-user-input.json#/properties/no_password_expiration")

### no\_password\_expiration Type

`boolean` ([No password expiration](alter-user-input-properties-no-password-expiration.md))

# alter-user input Definitions
