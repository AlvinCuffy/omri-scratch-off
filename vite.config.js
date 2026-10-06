import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import fs from 'fs'
import path from 'path'

// Custom Vite plugin to accept audio uploads from browser recording or file picker
function audioUploadPlugin() {
  return {
    name: 'audio-upload-handler',
    configureServer(server) {
      server.middlewares.use('/api/upload-audio', async (req, res, next) => {
        // Handle CORS preflight
        res.setHeader('Access-Control-Allow-Origin', '*')
        res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        res.setHeader('Access-Control-Allow-Headers', '*')

        if (req.method === 'OPTIONS') {
          res.writeHead(204)
          res.end()
          return
        }

        if (req.method === 'POST') {
          const chunks = []
          req.on('data', chunk => chunks.push(chunk))
          req.on('end', () => {
            const buffer = Buffer.concat(chunks)
            const targetDir = path.resolve(__dirname, 'audio')
            if (!fs.existsSync(targetDir)) {
              fs.mkdirSync(targetDir, { recursive: true })
            }

            // Save both as user_cloned_voice.mp3 and user_voice.m4a
            const targetMp3 = path.join(targetDir, 'user_cloned_voice.mp3')
            const targetM4a = path.join(targetDir, 'user_voice.m4a')
            const targetWav = path.join(targetDir, 'user_voice.wav')
            
            fs.writeFileSync(targetMp3, buffer)
            fs.writeFileSync(targetM4a, buffer)

            // Also copy to public/media
            const publicDir = path.resolve(__dirname, 'public/media')
            if (!fs.existsSync(publicDir)) {
              fs.mkdirSync(publicDir, { recursive: true })
            }
            fs.writeFileSync(path.join(publicDir, 'user_cloned_voice.mp3'), buffer)
            fs.writeFileSync(path.join(publicDir, 'user_voice.m4a'), buffer)

            console.log(`[Upload API] Successfully saved user voice file: ${buffer.length} bytes -> ${targetMp3}`)

            res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' })
            res.end(JSON.stringify({ 
              status: 'success', 
              message: 'Audio uploaded successfully!', 
              bytes: buffer.length,
              path: 'audio/user_cloned_voice.mp3' 
            }))
          })
        } else {
          next()
        }
      })
    }
  }
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), audioUploadPlugin()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: true,
    cors: true,
  },
  preview: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: true,
    cors: true,
  }
})
