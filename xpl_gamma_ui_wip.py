[
  {
    "selected" : false,
    "frame" : "{{0, 0}, {1024, 704}}",
    "class" : "View",
    "nodes" : [
      {
        "selected" : false,
        "frame" : "{{0, 0}, {1024, 704}}",
        "class" : "View",
        "nodes" : [

        ],
        "attributes" : {
          "flex" : "WH",
          "custom_class" : "scene.SceneView",
          "frame" : "{{70, 70}, {100, 100}}",
          "custom_attributes" : "{'scene':xploder()}",
          "class" : "View",
          "uuid" : "1336A2E3-E810-4026-8856-01138D5784AE",
          "name" : "scene"
        }
      },
      {
        "selected" : false,
        "frame" : "{{944, 60}, {80, 100}}",
        "class" : "View",
        "nodes" : [
          {
            "selected" : false,
            "frame" : "{{0, 0}, {80, 25}}",
            "class" : "Button",
            "nodes" : [

            ],
            "attributes" : {
              "alpha" : 1,
              "frame" : "{{10, 34}, {80, 32}}",
              "tint_color" : "RGBA(0.233333,0.488889,1.000000,1.000000)",
              "title" : "Run",
              "class" : "Button",
              "uuid" : "F2B7893F-C444-4321-91C7-A2DB62FE0CF3",
              "font_bold" : false,
              "font_size" : 15,
              "name" : "brun"
            }
          },
          {
            "selected" : false,
            "frame" : "{{0, 25}, {80, 25}}",
            "class" : "Button",
            "nodes" : [

            ],
            "attributes" : {
              "frame" : "{{0, 34}, {80, 32}}",
              "tint_color" : "RGBA(0.233333,0.488889,1.000000,1.000000)",
              "title" : "Pause",
              "class" : "Button",
              "uuid" : "388FA0C7-6CCF-4CCD-9AB6-DA6314AC08A3",
              "font_size" : 15,
              "name" : "bpause"
            }
          },
          {
            "selected" : false,
            "frame" : "{{0, 50}, {80, 25}}",
            "class" : "Button",
            "nodes" : [

            ],
            "attributes" : {
              "frame" : "{{0, 34}, {80, 32}}",
              "tint_color" : "RGBA(0.233333,0.488889,1.000000,1.000000)",
              "title" : "Reset",
              "class" : "Button",
              "uuid" : "A7185BE4-BC66-4160-BC39-0789CA3742B1",
              "font_size" : 15,
              "name" : "breset"
            }
          },
          {
            "selected" : true,
            "frame" : "{{0, 75}, {80, 25}}",
            "class" : "Button",
            "nodes" : [

            ],
            "attributes" : {
              "action" : "fsets",
              "frame" : "{{0, 34}, {80, 32}}",
              "tint_color" : "RGBA(0.233333,0.488889,1.000000,1.000000)",
              "title" : "Settings",
              "class" : "Button",
              "uuid" : "EA9FFB99-DBEF-4888-8A3F-BCD191FAEEE4",
              "font_size" : 15,
              "name" : "bsets"
            }
          }
        ],
        "attributes" : {
          "uuid" : "CC86B026-E8E6-4AF3-A396-8CCB01EFFBFD",
          "frame" : "{{190, 110}, {100, 100}}",
          "alpha" : 1,
          "class" : "View",
          "name" : "sceneb",
          "flex" : "LB"
        }
      },
      {
        "selected" : false,
        "frame" : "{{392, 0}, {240, 25}}",
        "class" : "View",
        "nodes" : [
          {
            "selected" : false,
            "frame" : "{{0, 0}, {240, 25}}",
            "class" : "Label",
            "nodes" : [

            ],
            "attributes" : {
              "name" : "label1",
              "text_color" : "RGBA(0.333333,0.555556,1.000000,1.000000)",
              "frame" : "{{45, -6}, {150, 32}}",
              "uuid" : "69ADBF62-AD24-4120-A076-A3738A464720",
              "text" : "Note: changing orientation of the device during simulation may cause improper behaviour.",
              "alignment" : "left",
              "class" : "Label",
              "font_size" : 10,
              "font_name" : "<System>"
            }
          }
        ],
        "attributes" : {
          "uuid" : "3956FDD2-48AD-4376-B360-9049BECA0B7D",
          "frame" : "{{190, 110}, {100, 100}}",
          "class" : "View",
          "name" : "view1",
          "flex" : "LR"
        }
      },
      {
        "selected" : false,
        "frame" : "{{988, 6}, {30, 30}}",
        "class" : "Button",
        "nodes" : [

        ],
        "attributes" : {
          "flex" : "LB",
          "action" : "sendhlep",
          "frame" : "{{472, 336}, {80, 32}}",
          "title" : "Button",
          "custom_attributes" : "{'image':ui.Image.named('questmark.png')}",
          "class" : "Button",
          "uuid" : "78FA4361-C7B2-424A-9C9F-04BE0B12ED42",
          "font_size" : 15,
          "name" : "bhlep"
        }
      },
      {
        "selected" : false,
        "frame" : "{{0, 0}, {1024, 704}}",
        "class" : "View",
        "nodes" : [
          {
            "selected" : false,
            "frame" : "{{974, 0}, {50, 25}}",
            "class" : "Button",
            "nodes" : [

            ],
            "attributes" : {
              "action" : "fback",
              "flex" : "L",
              "frame" : "{{200, 144}, {80, 32}}",
              "title" : "Back",
              "class" : "Button",
              "uuid" : "2758A91D-9229-4C6D-AD4F-56ABDB21504D",
              "font_size" : 15,
              "name" : "bback"
            }
          },
          {
            "selected" : true,
            "frame" : "{{242, 0}, {540, 704}}",
            "class" : "ScrollView",
            "nodes" : [
              {
                "selected" : false,
                "frame" : "{{0, 5}, {180, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label1",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "571CCC49-C4E3-4609-A36D-8D8235438388",
                  "text" : "Number of particles:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{180, 5}, {150, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "name" : "npart",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "36CC4E7E-CF47-4C24-9EBD-FF1671032AA7",
                  "text" : "50",
                  "alignment" : "right",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "autocorrection_type" : "no",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{330, 5}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "50",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "1D2C01F5-05DE-4EF1-B8C9-CFA013C0E3A9",
                  "custom_attributes" : "{'vars':['npart'],'vals':[50]}",
                  "font_size" : 15,
                  "name" : "button1"
                }
              },
              {
                "selected" : false,
                "frame" : "{{400, 5}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "200",
                  "class" : "Button",
                  "uuid" : "482076F7-E4D9-4829-A5DD-56041969CD04",
                  "custom_attributes" : "{'vars':['npart'],'vals':[200]}",
                  "font_bold" : true,
                  "font_size" : 15,
                  "name" : "button2"
                }
              },
              {
                "selected" : false,
                "frame" : "{{470, 5}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "1000",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "CEB719DB-E140-4ACC-B969-4DB25D3160BC",
                  "custom_attributes" : "{'vars':['npart'],'vals':[1000]}",
                  "font_size" : 15,
                  "name" : "button3"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 40}, {120, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "723F6E7A-85C2-485E-BFCE-E078523632B3",
                  "text" : "Ground zero:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label2",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{470, 40}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "gzcenter",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "Center",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2C98C75F-A4C8-441F-8DD1-7D1F3EC95F8A",
                  "custom_attributes" : "",
                  "font_size" : 15,
                  "name" : "button4"
                }
              },
              {
                "selected" : false,
                "frame" : "{{120, 40}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "EA8B8BF2-A9AA-42E5-90C1-887FA5D39C50",
                  "text" : "x:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label3",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{180, 40}, {110, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "font_name" : "<System>",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "02391499-932A-4048-A65A-9B5F6C543E3A",
                  "text" : "100",
                  "alignment" : "right",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "name" : "G0x",
                  "autocorrection_type" : "no"
                }
              },
              {
                "selected" : false,
                "frame" : "{{300, 40}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "C7CB5916-C227-48C7-AC41-10DF9DAA90FA",
                  "text" : "y:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label4",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{360, 40}, {110, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "font_name" : "<System>",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "9D9FA8BA-1DC7-4E5A-8BF8-FFC14DCFBB0E",
                  "text" : "100",
                  "alignment" : "right",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "name" : "G0y",
                  "autocorrection_type" : "no"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 75}, {120, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "6B5BE510-8310-455F-98A5-4DA2F7F586AC",
                  "text" : "Initial speed:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label5"
                }
              },
              {
                "selected" : false,
                "frame" : "{{120, 75}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "5E51D526-49E3-48E2-8603-BA7564FE1E13",
                  "text" : "mean:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label6",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{180, 75}, {110, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "vmu",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "0C88930D-56C4-4F81-8A66-D54DFCB4343F",
                  "text" : "1",
                  "alignment" : "right",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "autocorrection_type" : "no",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{300, 75}, {60, 32}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "E3B75E4E-8913-49E7-B213-87AA2BAA4131",
                  "text" : "sigma:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label7",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 145}, {120, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "0678085A-1CE2-4487-8389-274F8F337627",
                  "text" : "Velocity angle:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label8",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{360, 75}, {110, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "sigvmu",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "BA460413-1BC2-4F79-84A3-62DBCB591944",
                  "text" : "0",
                  "alignment" : "right",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "autocorrection_type" : "no",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{470, 75}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( 1; 0 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "BC5A5F9D-22A8-4AD7-9C2A-1ABADFEB1C38",
                  "custom_attributes" : "{'vars':['vmu','sigvmu'],'vals':[1,0], 'test':['lvsw',False]}",
                  "font_size" : 15,
                  "name" : "button5"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 110}, {99, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "D0ED8706-348A-4D03-A07E-2DFAF1301A0A",
                  "text" : "Custom:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label9"
                }
              },
              {
                "selected" : false,
                "frame" : "{{170, 110}, {370, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "9F70EBD8-4A5D-4B9C-A8A2-85A98A269E06",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing','enabled':False}",
                  "autocorrection_type" : "no",
                  "font_size" : 17,
                  "name" : "vfunc"
                }
              },
              {
                "selected" : false,
                "frame" : "{{109, 110}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "",
                  "action" : "msw_action",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "class" : "Switch",
                  "uuid" : "030C6EF2-34C2-4DE7-B24A-174D5A87FEBF",
                  "value" : false,
                  "custom_attributes" : "{'var':'lambdav','fields': ['vfunc','vmu','sigvmu']}",
                  "name" : "lvsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{120, 145}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "097FDA9E-B395-45EC-B533-AA629B0C11E6",
                  "text" : "mean:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label10",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{180, 145}, {110, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "7CE7BC6A-A9F7-4FF3-94E6-BF7EF9380698",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "-1",
                  "placeholder" : "",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "thmu",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{300, 145}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "8B262425-5108-4034-BDB7-48BB25D14253",
                  "text" : "sigma:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label11",
                  "font_size" : 18
                }
              },
              {
                "selected" : false,
                "frame" : "{{360, 145}, {110, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "alignment" : "right",
                  "font_name" : "<System>",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "text" : "0",
                  "class" : "TextField",
                  "uuid" : "44A0274D-56E8-4F20-ACC7-A7E4DB9F7728",
                  "autocorrection_type" : "no",
                  "font_size" : 17,
                  "name" : "sigthmu"
                }
              },
              {
                "selected" : false,
                "frame" : "{{470, 145}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( -1; 0 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "ACCA3763-FCCD-4247-8B26-782D7960A764",
                  "custom_attributes" : "{'vars':['thmu','sigthmu'],'vals':[-1,0], 'test':['lthsw',False]}",
                  "font_size" : 15,
                  "name" : "button6"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 180}, {99, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "DCDA8671-E7D9-4105-B2C1-5FE157C36C72",
                  "text" : "Custom:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label12",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{170, 180}, {370, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "1CC99141-6AC6-4A03-8371-FEE14A59945F",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing','enabled':False}",
                  "autocorrection_type" : "no",
                  "name" : "thfunc",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{109, 180}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'lambdath','fields': ['thfunc','thmu','sigthmu']}",
                  "class" : "Switch",
                  "value" : false,
                  "uuid" : "43F05703-1D09-4B22-8DCA-CB5D278AE748",
                  "name" : "lthsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 215}, {70, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label13",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "A4841058-5EB4-44AB-8FAB-41A0286C295F",
                  "text" : "Gravity:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{70, 215}, {30, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label14",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "CE72FB34-83C6-417E-B00C-8610835B2FE0",
                  "text" : "x:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{100, 215}, {95, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "gx",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "6F91AFD0-1846-423B-9D18-D286D5105928",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "text" : "0",
                  "autocorrection_type" : "no",
                  "alignment" : "right",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{235, 215}, {95, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "gy",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "BBA60606-C897-4169-8B4C-447F337A4E6F",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "text" : "0",
                  "autocorrection_type" : "no",
                  "alignment" : "right",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{205, 215}, {30, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label15",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "6F810FED-AE0A-482F-9640-D92148C431CD",
                  "text" : "y:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{330, 215}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( 0; 0 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "68EAFF66-8290-4748-A3A6-BC6C13F3B28F",
                  "custom_attributes" : "{'vars':['gx','gy'],'vals':[0,0]}",
                  "font_size" : 15,
                  "name" : "button7"
                }
              },
              {
                "selected" : false,
                "frame" : "{{400, 215}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( 0; -g )",
                  "uuid" : "894872B2-D17A-40F9-A386-B95E3D8F2A38",
                  "class" : "Button",
                  "font_bold" : true,
                  "custom_attributes" : "{'vars':['gx','gy'],'vals':[0,-9.81]}",
                  "name" : "button8",
                  "font_size" : 15
                }
              },
              {
                "selected" : false,
                "frame" : "{{470, 215}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( -6; -8 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "57C9EF89-04D7-4424-9742-9CD609AA4892",
                  "custom_attributes" : "{'vars':['gx','gy'],'vals':[-6,-8]}",
                  "font_size" : 15,
                  "name" : "button9"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 250}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "E9617C2B-1A7B-4424-B7F7-C28798A04063",
                  "text" : "Bounds:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label16",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{159, 250}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'boundson','fields': ['corb']}",
                  "class" : "Switch",
                  "value" : true,
                  "uuid" : "A47945B6-C81E-435B-9102-2E26596A2FEB",
                  "name" : "boundsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{220, 250}, {90, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "DA10E808-FD45-4954-B433-A5FA6529B4B3",
                  "text" : "CoR:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label17",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{310, 250}, {150, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "corb",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "9A482892-FD3A-4121-B727-84259D5907A1",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "text" : "1",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{500, 250}, {40, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "1",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2DD5C336-F223-453E-8716-66B8A215AB2D",
                  "custom_attributes" : "{'vars':['corb'],'vals':[1],'test':['boundsw',True]}",
                  "font_size" : 15,
                  "name" : "button10"
                }
              },
              {
                "selected" : false,
                "frame" : "{{460, 250}, {40, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "0",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2CFBCC95-711A-45CB-95A1-2D79230F3850",
                  "custom_attributes" : "{'vars':['corb'],'vals':[0],'test':['boundsw',True]}",
                  "font_size" : 15,
                  "name" : "button11"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 285}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "EB8C7DC0-EC97-4957-9053-A88BA39C1F7C",
                  "text" : "Collisions:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label18",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{159, 285}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'collson','fields': ['corp']}",
                  "class" : "Switch",
                  "value" : true,
                  "uuid" : "012AFC2C-AA48-446B-A6E1-74A9095B920A",
                  "name" : "collsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{310, 285}, {150, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "corp",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "13544008-C98B-44BB-A819-82FAD6011FB1",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "text" : "1",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{220, 285}, {90, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "2F482AC7-DEC2-46B0-8465-BCCAE46C018A",
                  "text" : "CoR:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label19",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{460, 285}, {40, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "0",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2CFBCC95-711A-45CB-95A1-2D79230F3850",
                  "custom_attributes" : "{'vars':['corp'],'vals':[0],'test':['collsw',True]}",
                  "font_size" : 15,
                  "name" : "button11"
                }
              },
              {
                "selected" : false,
                "frame" : "{{500, 285}, {40, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "1",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2CFBCC95-711A-45CB-95A1-2D79230F3850",
                  "custom_attributes" : "{'vars':['corp'],'vals':[1],'test':['collsw',True]}",
                  "font_size" : 15,
                  "name" : "button11"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 320}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "DDBA8C67-9815-4F3E-B5D1-8AF867BDC657",
                  "text" : "Air resistance:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label20",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{159, 320}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'airon','fields': ['airk']}",
                  "class" : "Switch",
                  "value" : false,
                  "uuid" : "012AFC2C-AA48-446B-A6E1-74A9095B920A",
                  "name" : "airsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{220, 320}, {50, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "59B365A6-B417-404F-958B-30A83BD09D6A",
                  "text" : "k:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label21",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{270, 320}, {150, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "0BB61856-E324-43C8-B028-88984E14E246",
                  "alignment" : "right",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS, 'enabled':False}",
                  "autocorrection_type" : "no",
                  "name" : "airk",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{420, 320}, {40, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "airkdec",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "E--",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "BBA37571-543B-4AF3-AA6E-26E41C9B6677",
                  "font_size" : 15,
                  "name" : "button12"
                }
              },
              {
                "selected" : false,
                "frame" : "{{460, 320}, {40, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "E0",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "5D9B8D08-4E1B-48FB-9171-4F28BF120F36",
                  "custom_attributes" : "{'vars':['airk'],'vals':[1],'test':['airsw',True]}",
                  "font_size" : 15,
                  "name" : "button13"
                }
              },
              {
                "selected" : false,
                "frame" : "{{500, 320}, {40, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "airkinc",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "E++",
                  "class" : "Button",
                  "uuid" : "D1FDC481-7E9B-467D-82DE-CE07D832D28C",
                  "font_size" : 15,
                  "name" : "button14"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 355}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label22",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "04905642-A6C6-4A51-A455-C06A39B5AA2A",
                  "text" : "Custom colours:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{159, 355}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'ccon','fields':  ['ccscheme','cctf1','cctf2','cctf3']}",
                  "class" : "Switch",
                  "value" : false,
                  "uuid" : "D0E34003-7E19-453E-942C-6C63C816DDFD",
                  "name" : "switch1"
                }
              },
              {
                "selected" : false,
                "frame" : "{{220, 355}, {320, 30}}",
                "class" : "SegmentedControl",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "LR",
                  "segments" : "H S V|R G B",
                  "frame" : "{{210, 256}, {120, 29}}",
                  "custom_attributes" : "{'enabled':False,'action':ccseg_action}",
                  "class" : "SegmentedControl",
                  "uuid" : "616ED552-A823-48DB-A4A4-A948C5850C6B",
                  "name" : "ccscheme"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 390}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "ccl1",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "BCBCDF1C-6200-445D-AC62-E8BBE3E587A7",
                  "text" : "H:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 425}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "ccl2",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "08CC42A8-0820-4C27-A723-45B541EF6D8F",
                  "text" : "S:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 460}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "ccl3",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "4EB620F1-6FC7-4725-94A9-8EF3D9E57BA8",
                  "text" : "V:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{60, 390}, {480, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "cctf1",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "7EA6BD7B-82F3-421B-9C8D-058043080AAD",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing', 'enabled':False}",
                  "autocorrection_type" : "no",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{60, 425}, {480, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "cctf2",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "C9FB0EB7-FF2A-41B9-AF13-6F12AB3F9A73",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing', 'enabled':False}",
                  "autocorrection_type" : "no",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{60, 460}, {480, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "cctf3",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "D7092619-0753-4AB0-B557-8B9C64D09119",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing', 'enabled':False}",
                  "autocorrection_type" : "no",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 495}, {540, 352}}",
                "class" : "View",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "H",
                  "frame" : "{{220, 220}, {100, 100}}",
                  "class" : "View",
                  "name" : "view1",
                  "uuid" : "10E4AE13-3681-4E19-9868-90AD531A7D52"
                }
              }
            ],
            "attributes" : {
              "border_width" : 0,
              "flex" : "HLR",
              "frame" : "{{352, 224}, {320, 320}}",
              "content_width" : 540,
              "content_height" : 847,
              "class" : "ScrollView",
              "uuid" : "94E9979F-3AC7-4FDB-B9CE-CB57F9DB1EF5",
              "corner_radius" : 0,
              "name" : "menu_ipad"
            }
          },
          {
            "selected" : false,
            "frame" : "{{10, 25}, {1004, 679}}",
            "class" : "ScrollView",
            "nodes" : [
              {
                "selected" : false,
                "frame" : "{{0, 5}, {169, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "571CCC49-C4E3-4609-A36D-8D8235438388",
                  "text" : "Number of particles:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label1",
                  "font_name" : "<System-Bold>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{170, 5}, {834, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "36CC4E7E-CF47-4C24-9EBD-FF1671032AA7",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "50",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "npart",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 40}, {335, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "WR",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "50",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "1D2C01F5-05DE-4EF1-B8C9-CFA013C0E3A9",
                  "custom_attributes" : "{'vars':['npart'],'vals':[50]}",
                  "font_size" : 15,
                  "name" : "button1"
                }
              },
              {
                "selected" : false,
                "frame" : "{{335, 40}, {335, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "WLR",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "200",
                  "class" : "Button",
                  "uuid" : "482076F7-E4D9-4829-A5DD-56041969CD04",
                  "custom_attributes" : "{'vars':['npart'],'vals':[200]}",
                  "font_bold" : true,
                  "font_size" : 15,
                  "name" : "button2"
                }
              },
              {
                "selected" : false,
                "frame" : "{{669, 40}, {335, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "WL",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "1000",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "CEB719DB-E140-4ACC-B969-4DB25D3160BC",
                  "custom_attributes" : "{'vars':['npart'],'vals':[1000]}",
                  "font_size" : 15,
                  "name" : "button3"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 75}, {120, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System-Bold>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "723F6E7A-85C2-485E-BFCE-E078523632B3",
                  "text" : "Ground zero:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label2"
                }
              },
              {
                "selected" : false,
                "frame" : "{{934, 75}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "gzcenter",
                  "flex" : "L",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "Center",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2C98C75F-A4C8-441F-8DD1-7D1F3EC95F8A",
                  "custom_attributes" : "",
                  "font_size" : 15,
                  "name" : "button4"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 110}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "EA8B8BF2-A9AA-42E5-90C1-887FA5D39C50",
                  "text" : "x:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label3"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 110}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "02391499-932A-4048-A65A-9B5F6C543E3A",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "100",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "G0x",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 145}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "C7CB5916-C227-48C7-AC41-10DF9DAA90FA",
                  "text" : "y:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label4"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 145}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "9D9FA8BA-1DC7-4E5A-8BF8-FFC14DCFBB0E",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "100",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "G0y",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 180}, {120, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System-Bold>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "6B5BE510-8310-455F-98A5-4DA2F7F586AC",
                  "text" : "Initial speed:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label5",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 215}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label6",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "5E51D526-49E3-48E2-8603-BA7564FE1E13",
                  "text" : "mean:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{60, 215}, {944, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "0C88930D-56C4-4F81-8A66-D54DFCB4343F",
                  "flex" : "W",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "1",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "vmu",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 250}, {60, 32}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label7",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "E3B75E4E-8913-49E7-B213-87AA2BAA4131",
                  "text" : "sigma:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 355}, {120, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label8",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "0678085A-1CE2-4487-8389-274F8F337627",
                  "text" : "Velocity angle:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System-Bold>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{60, 250}, {944, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "BA460413-1BC2-4F79-84A3-62DBCB591944",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "0",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "sigvmu",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{934, 180}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "L",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( 1; 0 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "BC5A5F9D-22A8-4AD7-9C2A-1ABADFEB1C38",
                  "custom_attributes" : "{'vars':['vmu','sigvmu'],'vals':[1,0], 'test':['lvsw',False]}",
                  "font_size" : 15,
                  "name" : "button5"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 285}, {99, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "D0ED8706-348A-4D03-A07E-2DFAF1301A0A",
                  "text" : "Custom:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label9",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 320}, {1004, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "font_name" : "<System>",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "9F70EBD8-4A5D-4B9C-A8A2-85A98A269E06",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing','enabled':False}",
                  "autocorrection_type" : "no",
                  "name" : "vfunc",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{948, 285}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "L",
                  "action" : "msw_action",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "class" : "Switch",
                  "uuid" : "030C6EF2-34C2-4DE7-B24A-174D5A87FEBF",
                  "value" : false,
                  "custom_attributes" : "{'var':'lambdav','fields': ['vfunc','vmu','sigvmu']}",
                  "name" : "lvsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 390}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "097FDA9E-B395-45EC-B533-AA629B0C11E6",
                  "text" : "mean:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label10"
                }
              },
              {
                "selected" : false,
                "frame" : "{{60, 390}, {944, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "7CE7BC6A-A9F7-4FF3-94E6-BF7EF9380698",
                  "flex" : "W",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "-1",
                  "placeholder" : "",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "thmu",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 425}, {60, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "8B262425-5108-4034-BDB7-48BB25D14253",
                  "text" : "sigma:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 18,
                  "name" : "label11"
                }
              },
              {
                "selected" : false,
                "frame" : "{{60, 425}, {944, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "44A0274D-56E8-4F20-ACC7-A7E4DB9F7728",
                  "flex" : "W",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "0",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "sigthmu",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{934, 355}, {70, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "L",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( -1; 0 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "ACCA3763-FCCD-4247-8B26-782D7960A764",
                  "custom_attributes" : "{'vars':['thmu','sigthmu'],'vals':[-1,0], 'test':['lthsw',False]}",
                  "font_size" : 15,
                  "name" : "button6"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 460}, {99, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label12",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "DCDA8671-E7D9-4105-B2C1-5FE157C36C72",
                  "text" : "Custom:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 495}, {1004, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "name" : "thfunc",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "1CC99141-6AC6-4A03-8371-FEE14A59945F",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing','enabled':False}",
                  "autocorrection_type" : "no",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{948, 460}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "flex" : "L",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'lambdath','fields': ['thfunc','thmu','sigthmu']}",
                  "class" : "Switch",
                  "value" : false,
                  "uuid" : "43F05703-1D09-4B22-8DCA-CB5D278AE748",
                  "name" : "lthsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 530}, {70, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "A4841058-5EB4-44AB-8FAB-41A0286C295F",
                  "text" : "Gravity:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label13",
                  "font_name" : "<System-Bold>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 565}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "CE72FB34-83C6-417E-B00C-8610835B2FE0",
                  "text" : "x:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label14",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 565}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "6F91AFD0-1846-423B-9D18-D286D5105928",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "0",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "gx",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 600}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "BBA60606-C897-4169-8B4C-447F337A4E6F",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "0",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "gy",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 600}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "6F810FED-AE0A-482F-9640-D92148C431CD",
                  "text" : "y:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label15",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{335, 635}, {334, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "WLR",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( 0; -9.81 )",
                  "uuid" : "894872B2-D17A-40F9-A386-B95E3D8F2A38",
                  "class" : "Button",
                  "font_bold" : true,
                  "custom_attributes" : "{'vars':['gx','gy'],'vals':[0,-9.81]}",
                  "name" : "button8",
                  "font_size" : 15
                }
              },
              {
                "selected" : false,
                "frame" : "{{669, 635}, {335, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "WL",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( -6; -8 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "57C9EF89-04D7-4424-9742-9CD609AA4892",
                  "custom_attributes" : "{'vars':['gx','gy'],'vals':[-6,-8]}",
                  "font_size" : 15,
                  "name" : "button9"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 670}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label16",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "E9617C2B-1A7B-4424-B7F7-C28798A04063",
                  "text" : "Bounds:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System-Bold>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{948, 670}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "flex" : "L",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'boundson','fields': ['corb']}",
                  "class" : "Switch",
                  "value" : true,
                  "uuid" : "A47945B6-C81E-435B-9102-2E26596A2FEB",
                  "name" : "boundsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 705}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label17",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "DA10E808-FD45-4954-B433-A5FA6529B4B3",
                  "text" : "CoR:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 705}, {914, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "9A482892-FD3A-4121-B727-84259D5907A1",
                  "flex" : "W",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "1",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "corb",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{979, 705}, {25, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "L",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "1",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2DD5C336-F223-453E-8716-66B8A215AB2D",
                  "custom_attributes" : "{'vars':['corb'],'vals':[1],'test':['boundsw',True]}",
                  "font_size" : 15,
                  "name" : "button10"
                }
              },
              {
                "selected" : false,
                "frame" : "{{954, 705}, {27, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "L",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "0",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2CFBCC95-711A-45CB-95A1-2D79230F3850",
                  "custom_attributes" : "{'vars':['corb'],'vals':[0],'test':['boundsw',True]}",
                  "font_size" : 15,
                  "name" : "button11"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 740}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label18",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "EB8C7DC0-EC97-4957-9053-A88BA39C1F7C",
                  "text" : "Collisions:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System-Bold>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{948, 740}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "flex" : "L",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'collson','fields': ['corp']}",
                  "class" : "Switch",
                  "value" : true,
                  "uuid" : "012AFC2C-AA48-446B-A6E1-74A9095B920A",
                  "name" : "collsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 775}, {914, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "13544008-C98B-44BB-A819-82FAD6011FB1",
                  "flex" : "W",
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "1",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "corp",
                  "font_size" : 17
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 775}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "name" : "label19",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "2F482AC7-DEC2-46B0-8465-BCCAE46C018A",
                  "text" : "CoR:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{954, 775}, {27, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "L",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "0",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2CFBCC95-711A-45CB-95A1-2D79230F3850",
                  "custom_attributes" : "{'vars':['corp'],'vals':[0],'test':['collsw',True]}",
                  "font_size" : 15,
                  "name" : "button11"
                }
              },
              {
                "selected" : false,
                "frame" : "{{979, 775}, {25, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "L",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "1",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "2CFBCC95-711A-45CB-95A1-2D79230F3850",
                  "custom_attributes" : "{'vars':['corp'],'vals':[1],'test':['collsw',True]}",
                  "font_size" : 15,
                  "name" : "button11"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 810}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System-Bold>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "DDBA8C67-9815-4F3E-B5D1-8AF867BDC657",
                  "text" : "Air resistance:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label20"
                }
              },
              {
                "selected" : false,
                "frame" : "{{948, 810}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "flex" : "L",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'airon','fields': ['airk']}",
                  "class" : "Switch",
                  "value" : false,
                  "uuid" : "012AFC2C-AA48-446B-A6E1-74A9095B920A",
                  "name" : "airsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 845}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_name" : "<System>",
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "59B365A6-B417-404F-958B-30A83BD09D6A",
                  "text" : "k:",
                  "alignment" : "left",
                  "class" : "Label",
                  "font_size" : 17,
                  "name" : "label21"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 845}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "0BB61856-E324-43C8-B028-88984E14E246",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "custom_attributes" : "{'keyboard_type':ui.KEYBOARD_NUMBERS, 'enabled':False}",
                  "alignment" : "right",
                  "autocorrection_type" : "no",
                  "text" : "0",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "name" : "airk",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 880}, {335, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "airkdec",
                  "flex" : "WR",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "E--",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "BBA37571-543B-4AF3-AA6E-26E41C9B6677",
                  "font_size" : 15,
                  "name" : "button12"
                }
              },
              {
                "selected" : false,
                "frame" : "{{335, 880}, {334, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "WLR",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "E0",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "5D9B8D08-4E1B-48FB-9171-4F28BF120F36",
                  "custom_attributes" : "{'vars':['airk'],'vals':[1],'test':['airsw',True]}",
                  "font_size" : 15,
                  "name" : "button13"
                }
              },
              {
                "selected" : false,
                "frame" : "{{669, 880}, {335, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "airkinc",
                  "flex" : "WL",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "E++",
                  "class" : "Button",
                  "uuid" : "D1FDC481-7E9B-467D-82DE-CE07D832D28C",
                  "font_size" : 15,
                  "name" : "button14"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 915}, {149, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "04905642-A6C6-4A51-A455-C06A39B5AA2A",
                  "text" : "Custom colours:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "label22",
                  "font_name" : "<System-Bold>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{948, 915}, {51, 31}}",
                "class" : "Switch",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "msw_action",
                  "flex" : "L",
                  "frame" : "{{245, 255}, {51, 31}}",
                  "custom_attributes" : "{'var':'ccon','fields':  ['ccscheme','cctf1','cctf2','cctf3']}",
                  "class" : "Switch",
                  "value" : false,
                  "uuid" : "D0E34003-7E19-453E-942C-6C63C816DDFD",
                  "name" : "ccsw"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 950}, {1004, 30}}",
                "class" : "SegmentedControl",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "segments" : "H S V|R G B",
                  "frame" : "{{210, 256}, {120, 29}}",
                  "custom_attributes" : "{'enabled':False,'action':ccseg_action}",
                  "class" : "SegmentedControl",
                  "uuid" : "616ED552-A823-48DB-A4A4-A948C5850C6B",
                  "name" : "ccscheme"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 985}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "BCBCDF1C-6200-445D-AC62-E8BBE3E587A7",
                  "text" : "H:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "ccl1",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 1020}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "08CC42A8-0820-4C27-A723-45B541EF6D8F",
                  "text" : "S:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "ccl2",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 1055}, {40, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "font_size" : 17,
                  "frame" : "{{195, 254}, {150, 32}}",
                  "uuid" : "4EB620F1-6FC7-4725-94A9-8EF3D9E57BA8",
                  "text" : "V:",
                  "alignment" : "left",
                  "class" : "Label",
                  "name" : "ccl3",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 985}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "7EA6BD7B-82F3-421B-9C8D-058043080AAD",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing', 'enabled':False}",
                  "autocorrection_type" : "no",
                  "name" : "cctf1",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 1020}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "C9FB0EB7-FF2A-41B9-AF13-6F12AB3F9A73",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing', 'enabled':False}",
                  "autocorrection_type" : "no",
                  "name" : "cctf2",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{40, 1055}, {964, 30}}",
                "class" : "TextField",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "font_size" : 17,
                  "frame" : "{{170, 254}, {200, 32}}",
                  "spellchecking_type" : "no",
                  "class" : "TextField",
                  "uuid" : "D7092619-0753-4AB0-B557-8B9C64D09119",
                  "alignment" : "left",
                  "custom_attributes" : "{'clear_button_mode':'while_editing', 'enabled':False}",
                  "autocorrection_type" : "no",
                  "name" : "cctf3",
                  "font_name" : "<System>"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 1090}, {1004, 415}}",
                "class" : "View",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "H",
                  "frame" : "{{220, 220}, {100, 100}}",
                  "class" : "View",
                  "name" : "view1",
                  "uuid" : "10E4AE13-3681-4E19-9868-90AD531A7D52"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 635}, {335, 30}}",
                "class" : "Button",
                "nodes" : [

                ],
                "attributes" : {
                  "action" : "mb_action",
                  "flex" : "WR",
                  "frame" : "{{230, 254}, {80, 32}}",
                  "title" : "( 0; 0 )",
                  "class" : "Button",
                  "font_bold" : true,
                  "uuid" : "68EAFF66-8290-4748-A3A6-BC6C13F3B28F",
                  "custom_attributes" : "{'vars':['gx','gy'],'vals':[0,0]}",
                  "font_size" : 15,
                  "name" : "button7"
                }
              }
            ],
            "attributes" : {
              "border_width" : 0,
              "flex" : "WH",
              "frame" : "{{352, 224}, {320, 320}}",
              "content_width" : 1004,
              "content_height" : 1500,
              "class" : "ScrollView",
              "uuid" : "94E9979F-3AC7-4FDB-B9CE-CB57F9DB1EF5",
              "corner_radius" : 0,
              "name" : "menu_iphone"
            }
          }
        ],
        "attributes" : {
          "flex" : "WH",
          "alpha" : 1,
          "frame" : "{{190, 110}, {100, 100}}",
          "class" : "View",
          "background_color" : "RGBA(0.898585,0.898585,0.898585,1.000000)",
          "uuid" : "A54CDB23-4107-4139-B26C-DF9E84606E8D",
          "custom_attributes" : "{'hidden':True}",
          "name" : "menushell"
        }
      },
      {
        "selected" : true,
        "frame" : "{{0, 0}, {1024, 704}}",
        "class" : "View",
        "nodes" : [
          {
            "selected" : false,
            "frame" : "{{974, 0}, {50, 25}}",
            "class" : "Button",
            "nodes" : [

            ],
            "attributes" : {
              "action" : "fback",
              "flex" : "L",
              "frame" : "{{472, 336}, {80, 32}}",
              "title" : "Back",
              "class" : "Button",
              "uuid" : "3851BBC5-DC05-49F6-B75F-286440B07DC7",
              "font_size" : 15,
              "name" : "enoughhlep"
            }
          },
          {
            "selected" : true,
            "frame" : "{{192, 0}, {640, 704}}",
            "class" : "ScrollView",
            "nodes" : [
              {
                "selected" : false,
                "frame" : "{{0, 50}, {640, 50}}",
                "class" : "TextView",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "EFE7CB31-5F53-402C-B28F-165E52EEF633",
                  "font_size" : 17,
                  "frame" : "{{220, 60}, {200, 200}}",
                  "editable" : false,
                  "alignment" : "center",
                  "autocorrection_type" : "default",
                  "text" : "Welcome to Xplodrrr! Here you will find the manual and release info.",
                  "font_name" : "<System-Bold>",
                  "spellchecking_type" : "default",
                  "class" : "TextView",
                  "name" : "textview1",
                  "flex" : "W"
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 0}, {640, 30}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "font_name" : "<System-Bold>",
                  "frame" : "{{245, 144}, {150, 32}}",
                  "uuid" : "E0183F02-1046-43B1-920C-7B75FBB47479",
                  "text" : "Xplodrrr v. Gamma",
                  "alignment" : "center",
                  "class" : "Label",
                  "name" : "label1",
                  "font_size" : 20
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 30}, {640, 20}}",
                "class" : "Label",
                "nodes" : [

                ],
                "attributes" : {
                  "flex" : "W",
                  "font_name" : "<System>",
                  "frame" : "{{245, 144}, {150, 32}}",
                  "uuid" : "43BAE949-4EBE-4380-AFBE-B7F6A68274BA",
                  "text" : "Build {} from {} running on iOS Pythonista",
                  "alignment" : "center",
                  "class" : "Label",
                  "name" : "verlab",
                  "font_size" : 12
                }
              },
              {
                "selected" : false,
                "frame" : "{{0, 100}, {640, 2000}}",
                "class" : "TextView",
                "nodes" : [

                ],
                "attributes" : {
                  "uuid" : "1C1E5250-A5B1-4B28-9A95-DD82309490B7",
                  "font_size" : 17,
                  "frame" : "{{220, 60}, {200, 200}}",
                  "editable" : false,
                  "alignment" : "left",
                  "autocorrection_type" : "no",
                  "text" : "Xplodrrr is a a simple 2D physics simulator. It simulates an \"explosion\", spread of a number of particles from a point under certain physical conditions.\n\n\nSIMULATION SCREEN\nBlack screen at the start is the simulation screen. \nButtons on the right control the sim and give access to it's settings.\nLabel in the lower left corner shows time passed in current simulation. If, during the simu process, it goes slower than normal clock, it means that your device is unable to process the sim with current settings quickly enough, I would suggest lowering number of particles.\n'Reset' button resets the sim, but NOT the settings.\nPressing 'Settings' and '?' buttons pauses the sim automatically.\nDuring the sim process, the buttons and labels will be dimmed, but they are always active.\nAlso during the process all of the settings are read-only. The developer finds it the most reasonable option.\n\n\nSETTINGS SCREEN\nNumeric fields accept any real numbers in either standard or scientific notation. Dot is expected as the decimal point. To avoid ambiguity, leaving a numeric field empty or entering an invalid value will cause the value to be set to 0.\nPressing a button with some value allows you to quckly set corresponding fields to that value. 'Center' button in GZ section sets GZ to current center point of the sim screen.\nThe 'E' buttons in air resistance section refer to scientific numeric notation, their actions left-to-right are: dividing the current value of k by 10, setting k to 1 and multiplying k by 10.\n'CoR' in bounds and collision sections are the corresponding coefficients of restitution. It is basically the measure of conservation energy in the collision. If you are not familiar with, but interested in the actual definition, here's a link to the Wiki article: https:\/\/en.m.wikipedia.org\/wiki\/Coefficient_of_restitution\nInitial speed and velocity angle are by default set for each particle via gaussian distribution with corresponding parameters.\nIMPORTANT: Negative angle mean will cause the angle to be uniformly random.\nAlso, evaluation of those values for each particle can be changed to a custom lambda function, if you enter it in the corresponding field. Note that leaving the field empty automatically sets the function to uniform random. The function should accept no arguments, yet you can kinda integrate internal variables of the sim scene if you read the source code a bit. Furthermore, you can use math, random and time modules in your function, if you need additional modules - append them to the import statement in the first line of the source code.\nThe same goes for customization of colours. Note that you can set either HSV or RGB colour schemes.\n\n\n\nThe developer is aware that there are still bugs in the simulation process, but he is just learning, so bear with him, please.\nDeveloped by Quadrohedron.\nUsing Pythonista developed by omz ( http:\/\/omz-software.com\/ ).\nDedicated to Maxwell Mordecai and Georgy Antonov.\n\n\nHope you have fun! ^^",
                  "font_name" : "<System>",
                  "spellchecking_type" : "no",
                  "class" : "TextView",
                  "name" : "hlepitself",
                  "flex" : "WH"
                }
              }
            ],
            "attributes" : {
              "flex" : "LR",
              "frame" : "{{352, 192}, {320, 320}}",
              "content_width" : 640,
              "content_height" : 2100,
              "class" : "ScrollView",
              "uuid" : "6124EBB4-4AAF-4667-8691-4698F7DB3143",
              "name" : "hlepitself"
            }
          }
        ],
        "attributes" : {
          "flex" : "WH",
          "frame" : "{{462, 302}, {100, 100}}",
          "custom_attributes" : "{'hidden':True}",
          "background_color" : "RGBA(0.898585,0.898585,0.898585,1.000000)",
          "class" : "View",
          "uuid" : "DC8216F2-15E6-4277-9995-7E42ECC50AC5",
          "name" : "hlepshell"
        }
      },
      {
        "selected" : false,
        "frame" : "{{0, 684}, {150, 20}}",
        "class" : "Label",
        "nodes" : [

        ],
        "attributes" : {
          "flex" : "T",
          "font_size" : 12,
          "text_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "frame" : "{{437, 336}, {150, 32}}",
          "uuid" : "E0B3AD63-6EF6-4EFA-8933-2BB3C882F370",
          "text" : "0.000",
          "alignment" : "left",
          "class" : "Label",
          "name" : "timelab",
          "font_name" : "<System>"
        }
      }
    ],
    "attributes" : {
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "enabled" : true,
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "name" : "name",
      "flex" : ""
    }
  }
]
