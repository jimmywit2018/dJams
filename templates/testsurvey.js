var surveyValueChanged = function (sender, options) {
    var el = document.getElementById(options.name);
    if (el) {
        el.value = options.value;
    }
};

var surveyQuestions = {
    questions: [
        {
            type: "text",
            name: "Username",
            isRequired: true,
            title: "What is your Spotify Username?:"

        }, {
          type: "text",
          name: "Email",
          isRequired: true,
          title: "What is your Google Email address?:"

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
              "Happy",
              "Sad",
              "Angry",
              "Surprise",
              "Fear"

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
        "Happy",
        "Sad",
        "Angry",
        "Surprise",
        "Fear"

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
    "Happy",
    "Sad",
    "Angry",
    "Surprise",
    "Fear"

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

window.survey = new Survey.Model(surveyQuestions);

survey
    .onComplete
    .add(function (result) {
        document
        .querySelector('#surveyResult')
        .innerHTML = "result: " + JSON.stringify(result.data);

    function encode( s ) {
        var out = [];
        for ( var i = 0; i < s.length; i++ ) {
            out[i] = s.charCodeAt(i);
        }
        return new Uint8Array( out );
    }

    var button = document.getElementById( 'button' );
    button.addEventListener( 'click', function() {

        var data = encode( JSON.stringify(result.data));


        var blob = new Blob( [ data ], {
            type: 'application/octet-stream'
        });

        url = URL.createObjectURL( blob );
        var link = document.createElement( 'a' );
        link.setAttribute( 'href', url );
        link.setAttribute( 'download', 'example.json' );

        var event = document.createEvent( 'MouseEvents' );
        event.initMouseEvent( 'click', true, true, window, 1, 0, 0, 0, 0, false, false, false, false, 0, null);
        link.dispatchEvent( event );
    });

        });




$("#surveyElement").Survey({model: survey, onValueChanged: surveyValueChanged});
