# Mastermind

Mastermind is an offensive security assessment agent.

## Docker Setup

```bash
docker run -ti --privileged --network host --name mastermind-kali kalilinux/kali-rolling
```

```bash
apt update && apt -y install kali-linux-headless

git clone https://github.com/Elfsong/mastermind.git

cd mastermind

uv venv

uv pip install deepagents-cli

deepagents
```