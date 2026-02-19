# whatiz 🔍

A lightweight CLI tool to get quick information about any topic right from your terminal using DuckDuckGo search.

## Features

**Lightning-fast information retrieval** - Get answers in one line  
**Uses DuckDuckGo** - No ads, no tracking (respects privacy)  

## Installation

### Using pip (Recommended)

```bash
pip install whatiz
```

The `whatiz` command will be automatically added to your PATH!

### Using pipx (For isolated environments)

```bash
pipx install whatiz
```

## Usage

Get quick information about anything:

```bash
whatiz python
whatiz climate change
whatiz quantum computing
whatiz "machine learning"
```

## Examples

```bash
$ whatiz blockchain
Blockchain is a distributed ledger technology that underlies cryptocurrencies like Bitcoin...

$ whatiz photosynthesis
Photosynthesis is the process by which plants convert light energy into chemical energy...

$ whatiz "dark matter"
Dark matter is a form of matter composed of particles that neither emit nor absorb light...
```

## How It Works

1. Takes your query from the command line
2. Searches using DuckDuckGo API (via `ddgs` library)
3. Returns the first result as a one-line summary
4. Displays it in your terminal

## Requirements

- Python 3.8+
- Internet connection (for search)

## Development

### Clone and setup

```bash
git clone https://github.com/yourusername/whatiz.git
cd whatiz
pip install -e ".[dev]"
```

### Install from source

```bash
pip install .
```

## Dependencies

- `ddgs` - DuckDuckGo search
- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing
- `sumy` - Text summarization
- `nltk` - Natural language processing
- `numpy` - Numerical computing

## Troubleshooting

**Command not found after installation?**
```bash
# Try this
python -m whatiz.main "your query"

# Or reinstall
pip install --force-reinstall whatiz
```

**Connection errors?**
- Check your internet connection
- DuckDuckGo servers might be temporarily down

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Your Name - [GitHub Profile](https://github.com/yourusername)

---

Made with ❤️ for the terminal enthusiasts
