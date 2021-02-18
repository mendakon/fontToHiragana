import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

# 使うフォント，サイズ，描くテキストの設定
ttfontname = "ここにフォントへのパスを入力"
fontsize = 253

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (256, 256)
backgroundRGBA = (255, 255, 255, 0)
textRGB       = (0, 0, 0)

texts = [{"yomi":"a","hira":"あ"},{"yomi":"i","hira":"い"},{"yomi":"u","hira":"う"},{"yomi":"e","hira":"え"},{"yomi":"o","hira":"お"},
{"yomi":"ka","hira":"か"},{"yomi":"ki","hira":"き"},{"yomi":"ku","hira":"く"},{"yomi":"ke","hira":"け"},{"yomi":"ko","hira":"こ"},
{"yomi":"sa","hira":"さ"},{"yomi":"si","hira":"し"},{"yomi":"su","hira":"す"},{"yomi":"se","hira":"せ"},{"yomi":"so","hira":"そ"},
{"yomi":"ta","hira":"た"},{"yomi":"ti","hira":"ち"},{"yomi":"tu","hira":"つ"},{"yomi":"te","hira":"て"},{"yomi":"to","hira":"と"},
{"yomi":"na","hira":"な"},{"yomi":"ni","hira":"に"},{"yomi":"nu","hira":"ぬ"},{"yomi":"ne","hira":"ね"},{"yomi":"no","hira":"の"},
{"yomi":"ha","hira":"は"},{"yomi":"hi","hira":"ひ"},{"yomi":"hu","hira":"ふ"},{"yomi":"he","hira":"へ"},{"yomi":"ho","hira":"ほ"},
{"yomi":"ma","hira":"ま"},{"yomi":"mi","hira":"み"},{"yomi":"mu","hira":"む"},{"yomi":"me","hira":"め"},{"yomi":"mo","hira":"も"},
{"yomi":"ya","hira":"や"},{"yomi":"yi","hira":"ゐ"},{"yomi":"yu","hira":"ゆ"},{"yomi":"ye","hira":"ゑ"},{"yomi":"yo","hira":"よ"},
{"yomi":"ra","hira":"ら"},{"yomi":"ri","hira":"り"},{"yomi":"ru","hira":"る"},{"yomi":"re","hira":"れ"},{"yomi":"ro","hira":"ろ"},
{"yomi":"wa","hira":"わ"},{"yomi":"wo","hira":"を"},{"yomi":"n", "hira":"ん"},{"yomi":"ten", "hira":"、"},{"yomi":"maru", "hira":"。"},
{"yomi":"ltu","hira":"っ"},
{"yomi":"lya","hira":"ゃ"},{"yomi":"lyu","hira":"ゆ"},{"yomi":"lyo","hira":"よ"},
{"yomi":"xa","hira":"ぁ"},{"yomi":"xi","hira":"ぃ"},{"yomi":"xu","hira":"ぅ"},{"yomi":"xe","hira":"ぇ"},{"yomi":"xo","hira":"ぉ"},
{"yomi":"onbiki","hira":"ー"},{"yomi":"bikkuri","hira":"！"},{"yomi":"hatena","hira":"？"},
{"yomi":"kakkoL","hira":"「"},{"yomi":"kakkoR","hira":"」"},
{"yomi":"ga","hira":"が"},{"yomi":"gi","hira":"ぎ"},{"yomi":"gu","hira":"ぐ"},{"yomi":"ge","hira":"げ"},{"yomi":"go","hira":"ご"},
{"yomi":"za","hira":"ざ"},{"yomi":"zi","hira":"じ"},{"yomi":"zu","hira":"ず"},{"yomi":"ze","hira":"ぜ"},{"yomi":"zo","hira":"ぞ"},
{"yomi":"da","hira":"だ"},{"yomi":"di","hira":"ぢ"},{"yomi":"du","hira":"ず"},{"yomi":"de","hira":"で"},{"yomi":"do","hira":"ど"},
{"yomi":"ba","hira":"ば"},{"yomi":"bi","hira":"び"},{"yomi":"bu","hira":"ぶ"},{"yomi":"be","hira":"べ"},{"yomi":"bo","hira":"ぼ"},]


for text in texts:
  # 文字を描く画像の作成
  img  = PIL.Image.new('RGBA', canvasSize, backgroundRGBA)
  draw = PIL.ImageDraw.Draw(img)

  # 用意した画像に文字列を描く
  font = PIL.ImageFont.truetype(ttfontname, fontsize)
  textWidth, textHeight = draw.textsize(text["hira"],font=font)
  top = 0
  left = 0
  bw = 3
  waku = (255,255,255)
  draw.text((top-bw, left-bw), text["hira"], fill=waku, font=font)
  draw.text((top-bw, left+bw), text["hira"], fill=waku, font=font)
  draw.text((top+bw, left-bw), text["hira"], fill=waku, font=font)
  draw.text((top+bw, left+bw), text["hira"], fill=waku, font=font)
  draw.text((top, left), text["hira"], fill=textRGB, font=font)

  img.save(f"hiraganas/hiragana_{text['yomi']}.png")

