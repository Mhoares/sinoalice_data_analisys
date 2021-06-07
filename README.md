# Sinoalice data analysis
Required:
* File with the info of the users in the same folder of the scripts with this schema
```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "guildUserData": {
          "type": "object",
          "properties": {
            "userId": {
              "type": "integer"
            },
            "guildDataId": {
              "type": "integer"
            },
            "guildPoint": {
              "type": "integer"
            },
            "guildRoleMstId": {
              "type": "integer"
            },
            "joinTime": {
              "type": "integer"
            },
            "isRemoveReservation": {
              "type": "integer"
            },
            "createdTime": {
              "type": "integer"
            },
            "updatedTime": {
              "type": "integer"
            }
          },
          "required": [
            "userId",
            "guildDataId",
            "guildPoint",
            "guildRoleMstId",
            "joinTime",
            "isRemoveReservation",
            "createdTime",
            "updatedTime"
          ]
        },
        "userData": {
          "type": "object",
          "properties": {
            "userId": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "playerId": {
              "type": "integer"
            },
            "comment": {
              "type": "string"
            },
            "currentCharacterMstId": {
              "type": "integer"
            },
            "currentJobMstId": {
              "type": "integer"
            },
            "currentJobRoleType": {
              "type": "integer"
            },
            "currentJobRolePosition": {
              "type": "integer"
            },
            "currentCostumeMstId": {
              "type": "integer"
            },
            "currentUserTitleMstId": {
              "type": "integer"
            },
            "currentTotalPower": {
              "type": "integer"
            },
            "gvgCharacterMstId": {
              "type": "integer"
            },
            "gvgJobMstId": {
              "type": "integer"
            },
            "gvgJobRoleType": {
              "type": "integer"
            },
            "gvgJobRolePosition": {
              "type": "integer"
            },
            "gvgTotalPower": {
              "type": "integer"
            },
            "gameStatus": {
              "type": "integer"
            },
            "level": {
              "type": "integer"
            },
            "leaderCardMstId": {
              "type": "integer"
            },
            "deckCost": {
              "type": "integer"
            },
            "maxCard": {
              "type": "integer"
            },
            "maxProtector": {
              "type": "integer"
            },
            "maxNightMare": {
              "type": "integer"
            },
            "maxOtherCard": {
              "type": "integer"
            },
            "maxStorageCard": {
              "type": "integer"
            },
            "maxStorageProtector": {
              "type": "integer"
            },
            "maxStorageNightMare": {
              "type": "integer"
            },
            "maxStorageOtherCard": {
              "type": "integer"
            },
            "maxItem": {
              "type": "integer"
            },
            "maxFriend": {
              "type": "integer"
            },
            "favoriteAkbMember1": {
              "type": "integer"
            },
            "favoriteAkbMember2": {
              "type": "integer"
            },
            "favoriteAkbMember3": {
              "type": "integer"
            },
            "isGameMaster": {
              "type": "integer"
            },
            "exp": {
              "type": "integer"
            },
            "stamina": {
              "type": "integer"
            },
            "staminaMax": {
              "type": "integer"
            },
            "staminaUpdatedTime": {
              "type": "integer"
            },
            "cleaningUpdatedTime": {
              "type": "integer"
            },
            "cleaningStatus": {
              "type": "integer"
            },
            "gvgWin": {
              "type": "integer"
            },
            "gvgLose": {
              "type": "integer"
            },
            "gvgDraw": {
              "type": "integer"
            },
            "gvgWinning": {
              "type": "integer"
            },
            "gvgMaxWinning": {
              "type": "integer"
            },
            "money": {
              "type": "integer"
            },
            "characterPoint": {
              "type": "integer"
            },
            "lastAccessTime": {
              "type": "integer"
            },
            "tutorialFinishTime": {
              "type": "integer"
            },
            "recentLoginTime": {
              "type": "string"
            },
            "maxMainLimitBreakSkill": {
              "type": "integer"
            },
            "maxSubLimitBreakSkill": {
              "type": "integer"
            },
            "isFrontRowChange": {
              "type": "boolean"
            },
            "createdTime": {
              "type": "integer"
            }
          },
          "required": [
            "userId",
            "name",
            "playerId",
            "comment",
            "currentCharacterMstId",
            "currentJobMstId",
            "currentJobRoleType",
            "currentJobRolePosition",
            "currentCostumeMstId",
            "currentUserTitleMstId",
            "currentTotalPower",
            "gvgCharacterMstId",
            "gvgJobMstId",
            "gvgJobRoleType",
            "gvgJobRolePosition",
            "gvgTotalPower",
            "gameStatus",
            "level",
            "leaderCardMstId",
            "deckCost",
            "maxCard",
            "maxProtector",
            "maxNightMare",
            "maxOtherCard",
            "maxStorageCard",
            "maxStorageProtector",
            "maxStorageNightMare",
            "maxStorageOtherCard",
            "maxItem",
            "maxFriend",
            "favoriteAkbMember1",
            "favoriteAkbMember2",
            "favoriteAkbMember3",
            "isGameMaster",
            "exp",
            "stamina",
            "staminaMax",
            "staminaUpdatedTime",
            "cleaningUpdatedTime",
            "cleaningStatus",
            "gvgWin",
            "gvgLose",
            "gvgDraw",
            "gvgWinning",
            "gvgMaxWinning",
            "money",
            "characterPoint",
            "lastAccessTime",
            "tutorialFinishTime",
            "recentLoginTime",
            "maxMainLimitBreakSkill",
            "maxSubLimitBreakSkill",
            "isFrontRowChange",
            "createdTime"
          ]
        },
        "guildUserConfigData": {
          "type": "object",
          "properties": {
            "guildUserConfigDataId": {
              "type": "integer"
            },
            "userId": {
              "type": "integer"
            },
            "rearguardGvgTimeType": {
              "type": "integer"
            },
            "invitationGvgJoinType": {
              "type": "integer"
            },
            "invitationGuildRankType": {
              "type": "integer"
            },
            "invitationActionType": {
              "type": "integer"
            },
            "invitationGvgTimeType": {
              "type": "integer"
            },
            "isInvitationSearch": {
              "type": "boolean"
            },
            "guildLanguageUserCode": {
              "type": "integer"
            },
            "guildCountryCode": {
              "type": "integer"
            }
          },
          "required": [
            "guildUserConfigDataId",
            "userId",
            "rearguardGvgTimeType",
            "invitationGvgJoinType",
            "invitationGuildRankType",
            "invitationActionType",
            "invitationGvgTimeType",
            "isInvitationSearch",
            "guildLanguageUserCode",
            "guildCountryCode"
          ]
        },
        "totalPower": {
          "type": "integer"
        },
        "maxHp": {
          "type": "integer"
        }
      },
      "required": [
        "guildUserData",
        "userData",
        "guildUserConfigData",
        "totalPower",
        "maxHp"
      ]
    }
  ]
}
```
