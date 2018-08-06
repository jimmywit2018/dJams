var surveyValueChanged = function (sender, options) {
    var el = document.getElementById(options.name);
    if (el) {
        el.value = options.value;
    }
};

var json = {
    questions: [
        {
            type: "text",
            name: "Username",
            isRequired: true,
            title: "What is your Spotify Username?:"

        }, {
            type: "checkbox",
            name: "types",
            title: "The type(s) of music I like are:",
            isRequired: true,
            colCount: 5,
            choices: [
              "Rock",
              "Jazz",
              "Country",
              "Pop",
              "Electronic"
            ]

            },

            {
              type: "checkbox",
              name: "sunnylisten",
              title: "When the weather is sunny, I typically listen to: (Click all that apply)",
              isRequired: true,
              colCount: 5,
              choices: [
                "Rock",
                "Jazz",
                "Country",
                "Pop",
                "Electronic"

            ]

          },

          {
            type: "checkbox",
            name: "sunnymood",
            title: "When the weather is sunny, the mood I am typically in is: (Click all that apply)",
            isRequired: true,
            colCount: 5,
            choices: [
              "Rock",
              "Jazz",
              "Country",
              "Pop",
              "Electronic"

          ]


      },

      {
        type: "checkbox",
        name: "rainylisten",
        title: "When the weather is rainy, I typically listen to: (Click all that apply)",
        isRequired: true,
        colCount: 5,
        choices: [
          "Rock",
          "Jazz",
          "Country",
          "Pop",
          "Electronic"

      ]

    },

    {
      type: "checkbox",
      name: "rainymood",
      title: "When the weather is rainy, the mood I am typically in is: (Click all that apply)",
      isRequired: true,
      colCount: 5,
      choices: [
        "Rock",
        "Jazz",
        "Country",
        "Pop",
        "Electronic"

    ]

  },

  {
    type: "checkbox",
    name: "cloudylisten",
    title: "When the weather is cloudy, I typically listen to: (Click all that apply)",
    isRequired: true,
    colCount: 5,
    choices: [
      "Rock",
      "Jazz",
      "Country",
      "Pop",
      "Electronic"

  ]

},

{
  type: "checkbox",
  name: "cloudymood",
  title: "When the weather is cloudy, the mood I am typically in is: (Click all that apply)",
  isRequired: true,
  colCount: 5,
  choices: [
    "Rock",
    "Jazz",
    "Country",
    "Pop",
    "Electronic"

]

},

{
  type: "checkbox",
  name: "workout",
  title: "When I am working out, I typically listen to: (Click all that apply)",
  isRequired: true,
  colCount: 5,
  choices: [
    "Rock",
    "Jazz",
    "Country",
    "Pop",
    "Electronic"

]

},

{
  type: "checkbox",
  name: "working",
  title: "When I'm working, I typically listen to: (Click all that apply)",
  isRequired: true,
  colCount: 5,
  choices: [
    "Rock",
    "Jazz",
    "Country",
    "Pop",
    "Electronic"

]

},

{
  type: "checkbox",
  name: "relaxing",
  title: "When I'm relaxing, I typically listen to: (Click all that apply)",
  isRequired: true,
  colCount: 5,
  choices: [
    "Rock",
    "Jazz",
    "Country",
    "Pop",
    "Electronic"

]





        }
    ]
};

window.survey = new Survey.Model(json);

survey
    .onComplete
    .add(function (result) {
        document

            .querySelector('#surveyResult')
            .innerHTML = "result: " + JSON.stringify(result.data);
    });



$("#surveyElement").Survey({model: survey, onValueChanged: surveyValueChanged});
