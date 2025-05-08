from flask import Flask, render_template, request

app = Flask(__name__)

# 定义自定义翻译词典
dictionary_ch = {
    '摸鱼': 'not paying attention or slacking off',
    '加油': 'keep going or good luck',
    '躺平': 'giving up on ambition and taking life easy',
    '内卷': 'involution or intense competition with no meaningful progress',
    '卷王': 'workaholic or overachiever in competitive environments',
    '凡尔赛': 'subtle bragging or humblebragging',
    '打工人': 'worker or working class hero',
    '996': 'working from 9 AM to 9 PM, 6 days a week',
    '社恐': 'social anxiety',
    '真香': 'it turned out better than expected',
    '硬核': 'hardcore or extremely skilled',
    '吃瓜群众': 'onlookers or people uninvolved watching drama',
    '鸽子': 'ghosting or not showing up as promised',
    '封神': 'legendary performance or surpassing expectations',
    '酸了': 'feeling jealous or envious',
    'emo': 'feeling emotional or down',
    '摆烂': 'purposefully doing poorly or giving up on something',
    '逆袭': 'a successful comeback or turnaround',
    '养生': 'health-conscious lifestyle or self-care',
    '破防': 'emotionally hurt or unable to withstand criticism',
    '白嫖': 'getting something for free without contributing',
    '炫富': 'showing off wealth or material possessions',
    '打卡': 'checking in (at a location or online)',
    '吃土': 'being broke or having no money',
    '上头': 'getting overly excited or obsessed',
    '大佬': 'boss, expert, or someone highly respected',
    '佛系': 'carefree or indifferent',
    '鸡汤': 'motivational speech or inspirational words',
}

dictionary_en = {
    'A birds eye view': '俯瞰',
    'Cat got your tongue': '你哑巴了吗?',
    'Dog eat dog': '残酷竞争',
    'Elephant in the room': '显而易见的问题',
    'Fish out of water': '格格不入',
    'Horse of a different color': '完全不同的事情',
    'Kill two birds with one stone': '一箭双雕',
    'Let the cat out of the bag': '泄露秘密',
    'Monkey business': '恶作剧',
    'Rat race': '激烈的竞争',
    'Break a leg': '祝你好运',
    'Cost an arm and a leg': '非常昂贵',
    'Get cold feet': '临阵退缩',
    'Head over heels': '非常爱',
    'Keep your head above water': '勉强度日',
    'Let your hair down': '放松',
    'Turn a blind eye': '视而不见',
    'Twist someones arm': '强迫某人做某事',
    'A piece of cake': '非常容易',
    'Bite off more than you can chew': '承担过多',
    'Bread and butter': '主要的生计',
    'Butter someone up': '奉承某人',
    'Spill the beans': '泄露秘密',
    'Take the cake': '最好或最坏',
    'A drop in the bucket': '微不足道',
    'A hot potato': '棘手的问题',
    'Beat around the bush': '拐弯抹角',
    'Hit the books': '努力学习',
    'Once in a blue moon': '非常罕见',
    'Raining cats and dogs': '大雨倾盆',
    'See eye to eye': '意见一致',
    'Throw in the towel': '放弃',
    'Under the weather': '不舒服',
    'Up in the air': '未定',
}
# 翻译函数
def custom_translate(text):
    translated_text = text
    for phrase, translation in dictionary_ch.items():
        translated_text = translated_text.replace(phrase, translation)
    return translated_text

# 主页路由，显示输入表单并处理翻译请求
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        translated_text = custom_translate(input_text)
        return render_template('index.html', input_text=input_text, translated_text=translated_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
