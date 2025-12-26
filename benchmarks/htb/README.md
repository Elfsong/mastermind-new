# HTB Benchmark

This benchmark is used to test the performance of the mastermind agent on the HTB platform.

## Setup

1. **API Token**: Obtain your HackTheBox API Token from your account settings (Profile > Settings > Create App Token).
2. **Environment Variable**: Add your token to the `.env` file in the project root:

```env
HTB_TOKEN=eyJ...
```

## Usage

The `htb.py` script provides a Python interface to the HackTheBox API via the `HTBEnv` class.

### Features

- `get_challenge_list()`: List available challenges.
- `get_challenge_info(challenge_id)`: Get details about a specific challenge.
- `get_challenge_file(challenge_id)`: Download challenge files.
- `post_challenge_start(challenge_id)`: Start a challenge instance.
- `post_challenge_flag(challenge_id, flag, difficulty)`: Submit a flag.

### Running

You can run the script using `uv`:

```bash
uv run benchmarks/htb/htb.py
```

*Note: The script currently contains example usage in the `if __name__ == "__main__":` block. Uncomment the lines you wish to execute.*
