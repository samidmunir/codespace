
import { createClient } from '@supabase/supabase-js'
const supabaseUrl = 'https://wulwmmzxynqhiewriymi.supabase.co'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind1bHdtbXp4eW5xaGlld3JpeW1pIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjM2MTkzNjMsImV4cCI6MjAzOTE5NTM2M30.8lTw0wFcJZyBZ8vEVHGNhwOAwOU81y3bJRxaj0jtGq4'
const supabase = createClient(supabaseUrl, supabaseKey)

export default supabase;