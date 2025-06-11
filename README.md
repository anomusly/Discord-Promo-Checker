# ⚡ DISCORD PROMO CHECKER v1

<p align="center">
  <img src="https://img.shields.io/badge/Status-FREE%20TOOL-green?style=for-the-badge" alt="status" />
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge" alt="platform" />
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge" alt="language" />
</p>

<p align="center">
  <b>🔥 Advanced Discord Promo Code Checker & Generator — FREE edition</b><br>
  🎉 Made with ❤️ by <a href="https://github.com/anomusly">@Hassan</a> | Discord Id <a href="https://discord.com/users/1136625769628581928">@Anomus.ly</a>
</p>

---

## ✨ Features

- ✅ **Multi-threaded processing** for faster promo checking
- 🔍 **Smart promo validation** (supports Discord & Xbox Game Pass promos)
- 🛡️ **Advanced proxy support** with auto-rotation
- 🚦 **Intelligent rate limiting** to prevent Discord API blocks
- 📊 **Real-time statistics** with colored console output
- 💾 **Auto-categorizes results** (Valid, Used, Invalid, Rate-limited)
- 🎯 **Pattern-based generator** for realistic promo codes
- ⚙️ **Highly configurable** via YAML config file
- 🔄 **Robust error handling** with exponential backoff
- 📝 **Detailed logging** with timestamps

---

## 📦 Installation

```bash
git clone https://github.com/anomusly/Discord-Promo-checker.git
cd Discord-Promo-checker
pip install -r requirements.txt
```

### 📋 Requirements

```
requests
tls-client
pystyle
colorama
PyYAML
```

---

## 🚀 Usage

### 🔍 Checking Promo Codes

1. **Add your Discord promo codes** to `Input/promos.txt`:
   ```
   https://promos.discord.gg/ABC123DEF456
   https://discord.com/billing/promotions/XYZ789
   ```

2. **Configure settings** in `config.yaml`:
   ```yaml
   Mask_Promo: true
   Print_Invalid: true
   Request_Delay: 2.5
   Force_Sequential: true
   ```

3. **Run the checker**:
   ```bash
   python main.py
   ```

4. **Enter number of threads** when prompted

5. **Check results** in the `output/` folder:
   - `valids.txt` - Working promo codes
   - `already_used.txt` - Previously redeemed codes
   - `invalid.txt` - Invalid/expired codes
   - `ratelimited.txt` - Rate-limited codes

### 🎲 Generating Promo Codes

1. **Run the generator**:
   ```bash
   python gen.py
   ```

2. **Follow the prompts** to configure generation

3. **Generated codes** will be saved to your specified file

---

<pre style="color: hotpink; font-weight: bold;">
             █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗██╗   ██╗███████╗
            ██╔══██╗████╗  ██║██╔═══██╗████╗ ████║██║   ██║██╔════╝
            ███████║██╔██╗ ██║██║   ██║██╔████╔██║██║   ██║███████╗
            ██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██║   ██║╚════██║
            ██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝███████║
            ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚══════╝
</pre>

## 🧾 Example Usage Flow

1. 📝 **Load promo codes** from `Input/promos.txt`
2. 🔍 **Validate each code** against Discord API
3. 📊 **Categorize results** (Valid/Used/Invalid/Rate-limited)
4. 💾 **Save organized results** to output files
5. 📈 **Display statistics** and completion summary

## ⚙️ Configuration Options

| Setting | Description | Default |
|---------|-------------|---------|
| `Mask_Promo` | Hide full promo codes in logs | `true` |
| `Print_Invalid` | Show invalid codes in console | `true` |
| `Update_Title` | Update console title with stats | `true` |
| `Use_Custom_Proxy` | Use custom proxy list | `false` |
| `Request_Delay` | Delay between requests (seconds) | `2.5` |
| `Max_Concurrent_Requests` | Max simultaneous requests | `1` |
| `Force_Sequential` | Force single-threaded mode | `true` |

## 🎯 Supported Promo Types

- 🎮 **Xbox Game Pass** Discord Nitro promos
- 👽 **Alienware** Discord partnership promos
- 🔗 **Generic Discord** promo codes
- 📱 **Mobile/Desktop** app promotions

## ⚠️ Important Notes

- 🚦 **Rate limiting is enforced** to prevent API blocks
- 🔄 **Sequential processing recommended** for stability
- �️ **Proxy rotation available** for enhanced anonymity
- ⏱️ **Exponential backoff** handles temporary rate limits
- 📊 **All results are automatically categorized** and saved

## 💸 Support Development

If this tool saved you time or helped you out, feel free to donate 💰:

**Litecoin (LTC)**: `ltc1qrw6ns4sxcngy9mjz8u96kn25clks858lwgtarr`

## 📞 Contact & Support

- 💬 **Discord**: `anomus.ly`
- 🛠️ **Custom Tools**: DM me on Discord with details and budget
- 🐛 **Issues**: Open an issue on GitHub

---

<p align="center">
  <b>⭐ If this tool helped you, please give it a star! ⭐</b>
</p>

