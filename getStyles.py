import random

def getFixedStyle():
  styles = {"poster_art":["album art","poster","layout","typography","logo","risograph","ghibli","Simon Stalenhag","insane detail","artstation","8K"],
  # "japanese":["ukiyoe","illustration","muted colors"],
  "ink" : ["black ink","hand drawn","minimal art","artstation","artgem","monochrome"],
  # "vangogh":["painting","by Van Gogh"],
  "steam_punk":["steampunk","stylized digital illustration","sharp focus","elegant","intricate","digital painting","artstation concept art","global illumination","ray tracing","advanced technology","Chaykin Howard","Campion Pascale","Cooke Darwyn","Davis jack","pink atmosphere"],
  "retro_wave":["illustration","retrowave art","neon lights","retro","digital art","trending on artstation"],
  "poly_art":["low poly","artstation","studio lighting","stainless steel","grey color scheme"],
  "vibrant":["psychedelic","water colors spots","vibrant color scheme","highly detailed","romanticism style","cinematic","artstation","greg Rutkowski"],
  "cinematic_render":["cinematic","dramatic colors","close-up","cgsociety","computer rendering","by mike Winkelmann","uhd","rendered in cinema4d","hard surface modeling","8k","render octane","inspired by beksinski"],
  "futuristic" : ["futuristic","elegant atmosphere","glowing lights","highly detailed","digital painting","artstation","concept art","smooth","sharp focus","illustration","art by wlop","mars ravelo","greg Rutkowski"],
  "mystical" : ["fireflies","deep focus","d&d","fantacy","intricate","elegant","highly detailed","digital painting","artstation","concept art","matte","sharp focus","illustration","hearthstone","greg Rutkowski","Alphonse Mucha","Andreas Rocha"],
  # "polaroid" : ["old polaroid","35mm"],
  # "picasso" : ["painting","by Pablo Picasso","cubism"],
  "sketch" : ["pencil","hand drawn","sketch","on paper"],
  "comic_book" : ["comic cover","1960's marvel comic","comic book illumination"],
  #######################################################
  # custom styles
  "caricature" :["caricature","hand drawn"],
  "robot" : ["purple pastel colors","super realistic","cinematic lighting","3D"],
  "pixar" : ["pixar","dreamworks","portrait","character design","soft cinematic lighting","8k","intricate details","pixar style character"],
  "color_smoke":["chaotic storm of twisting liquid","smoke portrait","by tom whalen","liam brazier","peter mohrbacher","artgem","shattered glass","bubbly underwater scenery","radiant light"],
  "disney_fantacy" : ["fantasy art","pixar","drawn by disney concept artists"," golden colour", "high quality", "highly detailed", "elegant", "sharp focus", "concept art", "character concepts", "digital painting","mystery", 'adventure'],
  "super_hero" : ["marvel superhero","background hyper detailed", "character design", "full body", "dynamic pose", "intricate","highly detailed", "digital painting", "artstation", "concept art", "smooth", "sharp focus", "illustration", "art by artgerm" , "greg rutkowski" , "alphonse mucha"],
  # "realaxing 3d":["3D render","red blush","wearing casual clothes","small smile","relaxing on a couch","cuddling up under a blanket","cozy living room","medium shot","8 k","octane render","artstation","artgerm","unreal engine 5","hyperrealism","hyperdetailed","ultra realistic"],
  # "style01" : ["Render" , "Cinema4d" , "Minimal" , "8K" , "Top POV" , "Pastal colors" , "Neon lights" , "Low Poly" , "Art Deco" , "Behance"],
  "style02" : ["illustration" , "Painting" , "Minimal" , "4K" , "Close-up" , "Pastal colors" , "Glowing lights" , "Mystical" , "Art Deco" , "Artgerm"],
  "style03" : ["illustration" , "Hand-Drawn" , "Intricate" , "4K" , "Landscape" , "Back and white" , "Dark lighting" , "Abstract" , "Futurism" , "Artstation "],
  "style04" : ["illustration" , "Drawing" , "caricature" , "Hyper - detailed" , "8K" , "Bottom POV" , "Vaporwave" , "Radiant" , "Futuristic" , "Futurism" , "Cgsociety"],
  "3dcharacters01" : ["Render" , "Render octane" , "Intricate" , "4K" , "Distance POV" , "Retrowave" , "Dramatic lighting" , "Psychedelic" , "Surrealism" , "Artstation"],
  "style06" : ["illustration" , "Print" , "Sticker" , "Hyper - realistic" , "High quality" , "Landscape" , "Pastal colors" , "Radiant" , "Fantacy" , "Surrealism" , "Pixiv"],
  "3dcharacters02" : ["Render" , "Render octane" , "Minimal" , "8K" , "Distance POV" , "Pastal colors" , "Radiant" , "Steampunk" , "Realistic" , "Cgsociety"],
  "photography01" : ["Photography" , "Deep focus" , "Hyper - detailed" , "4K" , "Bottom POV" , "Muted colors" , "Volumetric lighting" , "Fantacy" , "Realistic" , "Pixiv"],
  "vividViolet" : ["illustration" , "Digital art" , "Intricate" , "8K" , "Symmetrical" , "Vibrant colors" , "Glowing lights" , "Geometric" , "Cubism" , "Artstation"],
  "SoftRose" : ["illustration" , "Digital art" , "Hyper - realistic" , "4K" , "Distance POV" , "Pastal colors" , "Neon lights" , "Anime" , "Surrealism" , "Pixiv"],
  "style11" : ["illustration" , "Hand-Drawn" , "Hyper - detailed" , "8K" , "Close-up" , "Muted colors" , "Radiant" , "ukiyoe" , "Cubism" , "Artstation"],
  "style12" : ["Render" , "Render octane" , "Hyper - detailed" , "4K" , "Distance POV" , "Retrowave" , "Neon lights" , "Abstract" , "Cubism" , "Behance"],
  "photography02" : ["Photography" , "Sharp focus" , "Minimal" , "8K" , "Top POV" , "Dramatic colors" , "Glowing lights" , "Steampunk" , "Surrealism" , "Pixiv"],
  "style14" : ["illustration" , "Painting" , "Hyper - realistic" , "High quality" , "Bottom POV" , "Colorful" , "Radiant" , "Elegant" , "Realistic" , "Pixiv"],
  "style15" : ["Render" , "Product rendering" , "Styled" , "8K" , "Symmetrical" , "Vibrant colors" , "Cinematic lighting" , "Retro" , "Surrealism" , "Artstation "],
  "style15" : ["illustration" , "Hand-Drawn" , "Minimal" , "High quality" , "Top POV" , "Retrowave" , "Glowing lights" , "Futuristic" , "Cubism" , "Artgerm"],
  "colorfulWaterColor" : ["illustration" , "Drawing" , "Water Color" , "Intricate" , "4K" , "Symmetrical" , "Colorful" , "Cinematic lighting" , "Geometric" , "Cubism" , "Artgerm"],
  "softphoto" : ["Photography" , "35mm" , "Hyper - detailed" , "4K" , "Distance POV" , "Vibrant colors" , "Cinematic lighting" , "Elegant" , "Art Deco" , "Artstation "],
  "cartoon01" : ["illustration" , "Drawing" , "caricature" , "Intricate" , "4K" , "Distance POV" , "Complementary colors" , "Neon lights" , "Geometric" , "Surrealism" , "Cgsociety "],
  "style15" : ["Render" , "Product rendering" , "Hyper - realistic" , "4K" , "Bottom POV" , "Vibrant colors" , "Radiant" , "Retro" , "Realistic" , "Cgsociety"],
  "style15" : ["illustration" , "Street art" , "Minimal" , "8K" , "Close-up" , "Colorful" , "Dramatic lighting" , "Psychedelic" , "Surrealism" , "Artgerm"],
  "beautyOrange" : ["illustration" , "Painting" , "Styled" , "8K" , "Top POV" , "Colorful" , "Volumetric lighting" , "Mystical" , "Realistic" , "Behance"],
  "cyberpunk01" : ["portrait  " , "illustration" , "Digital art" , "Hyper - detailed" , "4K" , "Symmetrical" , "Complementary colors" , "Neon lights" , "Fantacy" , "Futurism" , "Artstation"],
  "metallic" : ["portrait " , "Render" , "Computer Rendering" , "Hyper - detailed" , "8K" , "Distance POV" , "Dramatic colors" , "Studio lighting" , "Futuristic" , "Realistic" , "Artstation"],
  "pastalMagazine" : ["illustration" , "Print" , "Graphic Novel" , "Hyper - realistic" , "8K" , "Close-up" , "Pastal colors" , "Studio lighting" , "Anime" , "Cubism" , "Cgsociety"],
  "photography03" : ["Photography" , "Expired film" , "Styled" , "4K" , "Close-up" , "Vibrant colors" , "Dark lighting" , "Smooth" , "Realistic" , "Artstation"],
  "caricature02" : ["illustration" , "Painting" , "Intricate" , "8K" , "Portrait" , "Vibrant colors" , "Radiant" , "Abstract" , "Realistic" , "Behance"],
  "posterVibe" : ["illustration" , "Hand-Drawn" , "Styled" , "High quality" , "Symmetrical" , "Complementary colors" , "Cinematic lighting" , "Retro" , "Cubism" , "Cgsociety"],
  "style19" : ["Render" , "Product rendering" , "Hyper - detailed" , "8K" , "Portrait" , "Dramatic colors" , "Studio lighting" , "Anime" , "Futurism" , "Pixiv"],
  "simple2dArt" : ["illustration" , "Hand-Drawn" , "Minimal" , "High quality" , "Distance POV" , "Retrowave" , "Dark lighting" , "Geometric" , "Realistic" , "Behance"],
  "3dDramatic" : ["Render" , "3D Render" , "Intricate" , "High quality" , "Symmetrical" , "Dramatic colors" , "Cinematic lighting" , "Fantacy" , "Cubism" , "Behance"],
  "pencil2" : ["illustration" , "Hand-Drawn" , "Hyper - detailed" , "8K" , "Bottom POV" , "Pastal colors" , "Dark lighting" , "Mystical" , "Futurism" , "Artstation"],
  "bwArt" : ["illustration" , "Digital art" , "Styled" , "8K" , "Portrait" , "Pastal colors" , "Cinematic lighting" , "Elegant" , "Futurism" , "Cgsociety"],
  "cyberpunk02" : ["illustration" , "Drawing" , "Ink" , "Hyper - detailed" , "4K" , "Landscape" , "Complementary colors" , "Cinematic lighting" , "Vaporwave" , "Cubism" , "Cgsociety"],
  "digitalPainting01" : ["illustration" , "Painting" , "Hyper - realistic" , "Low quality" , "Landscape" , "Pastal colors" , "Volumetric lighting" , "Anime" , "Surrealism" , "Pixiv"],
  "RealosticCgi" : ["Render" , "Product rendering" , "Minimal" , "4K" , "Close-up" , "Muted colors" , "Dramatic lighting" , "Futuristic" , "Cubism" , "Cgsociety"],
  "Bw2dArt" : ["Render" , "Computer Rendering" , "Minimal" , "4K" , "Top POV" , "Retrowave" , "Studio lighting" , "Mystical" , "Art Deco" , "Artgerm"],
  "mideaval" : ["Render" , "Product rendering" , "Styled" , "Low quality" , "Top POV" , "Muted colors" , "Radiant" , "Smooth" , "Realistic" , "Artgerm"],
  "egypthianFaroaa" : ["illustration" , "Painting" , "Intricate" , "High quality" , "Close-up" , "Pastal colors" , "Glowing lights" , "Futuristic" , "Surrealism" , "Behance"],
  "photography04" : ["Photography" , "Cinematic" , "Hyper - realistic" , "4K" , "Symmetrical" , "Dramatic colors" , "Radiant" , "Smooth" , "Art Deco" , "Artgerm"],
  "darksteampunk" : ["Render" , "Computer Rendering" , "Intricate" , "High quality" , "Distance POV" , "Pastal colors" , "Dark lighting" , "Steampunk" , "Cubism" , "Cgsociety-"],
  "style20" : ["illustration" , "Digital art" , "Hyper - detailed" , "High quality" , "Symmetrical" , "Back and white" , "Radiant" , "Mystical" , "Surrealism" , "Artstation"],
  "photography05" : ["Photography" , "Deep focus" , "Hyper - realistic" , "High quality" , "Portrait" , "Colorful" , "Volumetric lighting" , "Elegant" , "Cubism" , "Behance"],
  "photography06" : ["Photography" , "Deep focus" , "Hyper - detailed" , "4K" , "Symmetrical" , "Complementary colors" , "Dark lighting" , "Futuristic" , "Surrealism" , "Behance"],
  "hyperRender" : ["Render" , "Cinema4d" , "Hyper - realistic" , "8K" , "Bottom POV" , "Pastal colors" , "Dramatic lighting" , "Anime" , "Cubism" , "Artgerm"],
  # "style21" : ["Render" , "Render octane" , "Styled" , "4K" , "Portrait" , "Muted colors" , "Volumetric lighting" , "Low Poly" , "Futurism" , "Artgerm"],
  "style22" : ["Render" , "Render octane" , "Hyper - detailed" , "8K" , "Landscape" , "Muted colors" , "Dramatic lighting" , "Elegant" , "Realistic" , "Pixiv"],
  "electricGlow" : ["illustration", "Digital art", "Hyper - realistic", "High quality", "Distance POV", "Complementary colors", "Volumetric lighting", "Mystical", "Futurism", "Artstation"],
  "Photography07" : ["Photography", "Expired film", "Intricate", "4K", "Landscape", "Retrowave", "Dramatic lighting", "Abstract", "Futurism", "Artgerm"],
  "Photography08" : ["Render", "Product rendering", "Hyper - realistic", "High quality", "Symmetrical", "Dramatic colors", "Glowing lights", "Geometric", "Realistic", "Cgsociety"],
  "jocker" : ["Render", "Cinema4d", "Hyper - realistic", "8K", "Distance POV", "Muted colors", "Neon lights", "Elegant", "Cubism", "Behance"],
  "CyanFuture" : ["Render", "Computer Rendering", "Hyper - detailed", "4K", "Top POV", "Vaporwave", "Neon lights", "Smooth", "Futurism", "Pixiv"],
  "Photography09" : ["Photography", "35mm", "Hyper - detailed", "8K", "Top POV", "Dramatic colors", "Volumetric lighting", "Psychedelic", "Realistic", "Artstation"],
  "dramaticBW" : ["Photography", "35mm", "Intricate", "High quality", "Portrait", "Dramatic colors", "Dramatic lighting", "Futuristic", "Realistic", "Cgsociety"],
  "animeStreetArt" : ["illustration", "Street art", "Hyper - detailed", "High quality", "Landscape", "Complementary colors", "Neon lights", "Anime", "Surrealism", "Behance"],
  "3dCyberpunk" : ["Render", "Render octane", "Intricate", "4K", "Top POV", "Complementary colors", "Neon lights", "Elegant", "Art Deco", "Cgsociety"],
  "PastalPhotography" : ["Photography", "Expired film", "Intricate", "8K", "Top POV", "Pastal colors", "Dark lighting", "Smooth", "Art Deco", "Artstation"],
  "WaxSculpture" : ["Render", "3D Render", "Hyper - realistic", "8K", "Distance POV", "Back and white", "Dramatic lighting", "Futuristic", "Futurism", "Artgerm"],
  "cartoonSyle" : ["illustration", "Drawing", "caricature", "Minimal", "High quality", "Landscape", "Muted colors", "Neon lights", "Psychedelic", "Art Deco", "Behance"],
  "3dcharacters03" : ["Render", "Render octane", "Hyper - realistic", "8K", "Top POV", "Pastal colors", "Studio lighting", "Futuristic", "Realistic", "Pixiv"],
  "minimalSimpleArt" : ["illustration", "Hand-Drawn", "Minimal", "4K", "Portrait", "Cubism", "Pixiv"],
  "bwRender" : ["Render", "Product rendering", "Back and white", "Art Deco"],
  "sticker" : ["illustration", "Hand-Drawn", "Styled", "4K", "Distance POV", "Muted colors", "Dark lighting"],
  "photography07" : ["Photography", "old photo", "Minimal", "8K", "Close-up", "Muted colors", "Dark lighting"],
  "photography08" : ["Photography", "200mm", "Styled", "Geometric", "Surrealism"],
  "characterDesign01" : ["Render", "character design ", "Cinema4d", "Hyper - detailed", "Close-up", "Radiant", "Futuristic"],
  "characterDesign02" : ["Render,haracter design", "Render octane", "Hyper - realistic", "Distance POV", "Back and white", "Steampunk"],
  "characterDesign03" : ["Render", "Product rendering", "8K", "Bottom POV", "Glowing lights"],
  "photography09" : ["Photography", "Deep focus", "Styled", "High quality", "Landscape", "Dramatic colors", "Dark lighting", "Artgerm"],
  "cyberpunk03" : ["fireflies", "glow", "volumetric lighting - illustration", "Digital art", "Hyper - detailed", "8K", "Bottom POV", "Dark lighting", "Art Deco"],
  "digitalPainting02" : [" illustration", "Digital art", "High quality", "Bottom POV", "Volumetric lighting"],
  "bwRender02" : ["Render", "Render octane", "Hyper - detailed", "8K", "Landscape", "Back and white", "Studio lighting", "Mystical"],
  "photography10" : ["Photography", "Sharp focus", "Styled", "4K", "Pastal colors", "Glowing lights", "Elegant", "Realistic"],
  "realisticCgi2" : ["Render", "3D Render", "Symmetrical", "Behance"],
  "photography11" : ["Photography", "old photo", "Hyper - realistic", "High quality", "Symmetrical", "Neon lights", "Smooth", "Realistic", "Pixiv"],
  "streetart01" : ["illustration", "Street art", "Intricate", "4K", "Colorful", "Glowing lights", "Mystical", "Futurism"],
  "strokedPainting" : ["illustration", "Painting", "Styled", "4K", "Symmetrical", "Muted colors", "Cinematic lighting", "Art Deco"],
  "FadedBWPhotography" : ["Photography", "200mm", "High quality", "Portrait", "Glowing lights", "Geometric", "Behance"],
  "retroRender01" : ["Render", "Computer Rendering", "4K", "Close-up", "Retrowave", "Realistic"],
  "pastalRender" : ["Render", "Computer Rendering", "Styled", "4K", "Pastal colors", "Art Deco", "Artstation"],
  "styledRender" : ["Render", "3D Render", "Styled", "4K", "Top POV", "Vaporwave", "Neon lights", "Art Deco"],
  "photography12" : ["Photography", "Deep focus", "8K", "Dramatic lighting", "Artstation"],
  "photography13" : ["Photography", "old photo", "Styled", "8K", "Landscape", "Vibrant colors", "Fantacy"],
  "cinema4dRender" : ["Render", "Cinema4d", "Intricate", "4K", "Top POV", "Dramatic lighting", "Futurism", "Artgerm "],
  "Bwphotography14" : ["Photography", "Deep focus", "8K", "Landscape", "Back and white", "Dark lighting", "Psychedelic", "Pixiv"]
  }
  
  key = random.choice([*styles.keys()])
  style = " , ".join(styles[key])
  return key,style


def getRandomStyle():
  # artwork = ["illustration","Render","Photography"]
  # illustration_type=["Drawing","Painting","Digital art","Print","Hand-Drawn","Street art"]
  # drawing_type=["Water Color","Pencil","Ink"]
  # printing_type=["Comic Book","Graphic Novel","Magazine","Poster","Postage stamp","Sticker"]
  # render_type=["3D Render","Product rendering","Render octane","Cinema4d","Computer Rendering"]
  # photography_type=["polaroid","old photo","35mm","Macro","Cinematic","Sharp focus","Deep focus","200mm","Expired film"]

  detail = ["Hyper - realistic","Hyper - detailed","Intricate","Minimal","Styled"]
  Resolution =["8K","4K","High quality"]
  perspective = ["Portrait","Landscape","Bottom POV","Top POV","Distance POV","Close-up","Symmetrical"]
  color_scheme=["Pastal colors","Complementary colors","Muted colors","Vibrant colors","Dramatic colors","Vaporwave","Retrowave","Back and white","Colorful","Autochrome"]
  lighting=["Radiant","Neon lights","Glowing lights","Cinematic lighting","Dramatic lighting","Dark lighting","Volumetric lighting","Studio lighting"]
  styles=["Mystical","Elegant","Futuristic","Abstract","Vaporwave","Retro","Steampunk","Geometric","Low Poly","Psychedelic","Smooth","Fantacy","Anime","ukiyoe"]
  asrtistic_movement=["Realistic","Cubism","Surrealism","Futurism","Art Deco"]
  trending = ["Artstation","Pixiv","Cgsociety","Artgerm","Behance"]

  image_type = {
      "illustration":{
          "Drawing":["Water Color","Pencil","Ink","caricature","charcoal"],
          "Painting":[],
          "Digital art":[],
          "Print":["Comic Book","Graphic Novel","Magazine","Poster","Postage stamp","Sticker"],
          "Hand-Drawn":[],
          "Street art":[]
          },
      "Render":{
          "3D Render":[],
          "Product rendering":[],
          "Render octane":[],
          "Cinema4d":[],
          "Computer Rendering":[]
      },
      "Photography":{
          # "polaroid":[],
          "canon m50":[],
          "old photo":[],
          "35mm":[],
          # "Macro":[],
          "Cinematic":[],
          "Sharp focus":[],
          "Deep focus":[],
          "200mm":[],
          "Expired film":[]
      }
  }

  style = ""
  style = style if (random.choice([True,True,True,False])==False) else f"{style}, {random.choice(detail)}"
  style = style if (random.choice([True,True,True,False])==False) else f"{style}, {random.choice(Resolution)}"

  type1 = random.choice([*image_type.keys()])
  type2 = random.choice([*image_type[type1].keys()])
  style=f"{style}, {type1}, {type2}"
  if len(image_type[type1][type2])>0:
    type3 = random.choice(image_type[type1][type2])
    style=f"{style}, {type3}"
  

  style = style if (random.choice([True,True,False])==False) else f"{style}, {random.choice(perspective)}"
  style = style if (random.choice([True,True,False])==False) else f"{style}, {random.choice(color_scheme)}"
  style = style if (random.choice([True,True,True,True,False])==False) else f"{style}, {random.choice(lighting)}"
  style = style if (random.choice([True,True,False])==False) else f"{style}, {random.choice(styles)}"
  style = style if (random.choice([True,False])==False) else f"{style}, {random.choice(asrtistic_movement)}"
  style = style if (random.choice([True,False])==False) else f"{style}, {random.choice(trending)}"

  return style 
