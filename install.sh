
#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "================================"
echo "       STARX TERMINAL V2"
echo "        INSTALLER"
echo "================================"

pkg install python curl -y

mkdir -p "$HOME/STARX-TERMINAL-V2"
mkdir -p "$HOME/bin"

curl -fL \
"https://raw.githubusercontent.com/zulnul4-dot/STARX-TERMINAL-v2/main/main.py" \
-o "$HOME/STARX-TERMINAL-V2/main.py"

cat > "$HOME/bin/RUN-STARX" <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash
exec python "$HOME/STARX-TERMINAL-V2/main.py" "$@"
EOF

chmod +x "$HOME/bin/RUN-STARX"

grep -qxF 'export PATH="$HOME/bin:$PATH"' "$HOME/.bashrc" 2>/dev/null || \
echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"

export PATH="$HOME/bin:$PATH"

echo ""
echo "STARX TERMINAL V2 INSTALLED!"
echo "Type RUN-STARX to launch."
