const {
    default: makeWASocket,
    useMultiFileAuthState
} = require("@whiskeysockets/baileys")
const fs = require("fs")
const path = require("path")
const readline = require("readline")
const chalk = require("chalk")
const pino = require("pino") // ini wajib di atas

async function startBot() {
    const { state, saveCreds } = await useMultiFileAuthState("session")
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false, // karena pake pairing code
        logger: pino({ level: "silent" })
    })

    // 🔥 Pairing Code kalau belum login
    if (!sock.authState.creds.registered) {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        })
        rl.question("Masukkan nomor WhatsApp (62xxx): ", async (number) => {
            const code = await sock.requestPairingCode(number)
            console.log(chalk.green(`\n🔥 Pairing Code: ${code}\n`))
            rl.close()
        })
    }

    // Simpan session
    sock.ev.on("creds.update", saveCreds)

    // Event koneksi
    sock.ev.on("connection.update", (update) => {
        const { connection } = update
        if (connection === "open") {
            console.log(chalk.green("✅ Bot connected!"))
        } else if (connection === "close") {
            console.log(chalk.red("❌ Bot disconnected, mencoba ulang..."))
            startBot()
        }
    })

    // Load & jalankan semua plugin
    function loadPlugins(msg, text) {
        fs.readdirSync("./plugins").forEach(file => {
            if (file.endsWith(".js")) {
                try {
                    delete require.cache[require.resolve(path.join(__dirname, "plugins", file))]
                    require(path.join(__dirname, "plugins", file))(sock, msg, text)
                } catch (e) {
                    consol
