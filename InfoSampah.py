import discord
from discord.ext import commands
import random
from model import get_class

TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

#Infos.

info_organic_text = """
**Sampah Organik**:
Sampah organik berasal dari bahan yang bisa terurai alami seperti sisa makanan dan daun kering.
- **Manfaat**: Sampah organik dapat dijadikan kompos untuk memperkaya tanah dan mengurangi limbah.
- **Contoh**: Kulit buah, sayuran sisa, daun, ampas kopi.
"""

info_non_organic_text = """
**Sampah Non-Organik**:
Sampah non-organik adalah bahan yang sulit terurai dan perlu didaur ulang dengan cara khusus.
- **Tantangan**: Sampah non-organik bisa mencemari lingkungan karena butuh waktu lama untuk terurai.
- **Contoh**: Plastik, logam, kaca, kain sintetis.
"""

info_recyclable_text = """
**Bahan yang Bisa Didaur Ulang**:
Bahan daur ulang adalah barang yang bisa diproses ulang dan digunakan kembali untuk mengurangi sampah.
- **Penting**: Daur ulang membantu menghemat bahan baku dan mengurangi pencemaran.
- **Contoh**: Kertas, kardus, plastik tertentu, logam, kaca.
"""

info_hazardous_text = """
**Sampah Berbahaya**:
Sampah berbahaya adalah bahan yang dapat merusak lingkungan atau kesehatan jika dibuang sembarangan.
- **Pengelolaan**: Harus dibuang dengan hati-hati untuk menghindari pencemaran dan risiko kesehatan.
- **Contoh**: Baterai, bahan kim    ia, sampah medis, barang elektronik.
"""

opinions = [
    """
**Pendapat 1**: Fokus pada gaya hidup tanpa sampah (zero-waste). Dengan mengurangi penggunaan plastik sekali pakai, 
kompos, dan membawa wadah sendiri, kita bisa mengurangi sampah secara individu.
    """,

    """
**Pendapat 2**: Investasi dalam teknologi daur ulang. Teknologi yang lebih baik bisa memproses sampah lebih efisien 
dan membantu mengubah sampah yang tidak dapat didaur ulang menjadi energi.
    """,

    """
**Pendapat 3**: Terapkan kebijakan ketat untuk mengurangi sampah. Pemerintah bisa membatasi produksi plastik, menaikkan target daur ulang, 
dan memberi insentif bagi produk ramah lingkungan.
    """
]

helpme_text = """
**Commands**:
1. `!infoorganic` - Informasi tentang sampah organik.
2. `!infononorganic` - Informasi tentang sampah non-organik.
3. `!inforecyclable` - Informasi tentang bahan yang bisa didaur ulang.
4. `!infohazardous` - Informasi tentang sampah berbahaya.
5. `!saveearth` - Opini acak tentang cara menyelamatkan bumi dari sampah.
"""

#Commands

@bot.command(name='infoorganic')
async def info_organic(ctx):
    await ctx.send(info_organic_text)

@bot.command(name='infononorganic')
async def info_non_organic(ctx):
    await ctx.send(info_non_organic_text)

@bot.command(name='inforecyclable')
async def info_recyclable(ctx):
    await ctx.send(info_recyclable_text)

@bot.command(name='infohazardous')
async def info_hazardous(ctx):
    await ctx.send(info_hazardous_text)

@bot.command(name='helpme')
async def helpme_command(ctx):
    await ctx.send(helpme_text)
@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'./{file_name}')
            await ctx.send(f'file berhasil disimpan: {file_name}')
            await ctx.send(f'file bisa di akses di cloud discord: {file_url}')
        
        kelas, skor = get_class('keras_model.h5', 'labels.txt',f'./{file_name}')

        if kelas == '0 High Five' and skor >= 0.75:
            await ctx.send('ini adalah High Five ')
            await ctx.send('Penjelasan: High Five adalah gerakan di mana tangan terbuka diangkat untuk ditepukkan dengan tangan orang lain, biasanya sebagai bentuk semangat atau perayaan.')

        elif kelas == '1 Fist Up' and skor >= 0.75:
            await ctx.send('ini adalah Fist Up')
            await ctx.send('Penjelasan: Fist Up adalah gerakan mengepalkan tangan dan mengangkatnya ke atas, sering digunakan sebagai simbol kekuatan, solidaritas, atau dukungan.')

        else:
            await ctx.send('aku tidak tahu apa ini')

# Run the bot

bot.run("MTMwMDgwODYxNDg0NzU3ODIxMg.G1zejS.SmhGaekvD1_xz16kWI3GuZT8ronNStto4rLK_I")
