import { GoogleGenerativeAI } from '@google/generative-ai';

const genAI = new GoogleGenerativeAI("AIzaSyDWFmyny36jYVIcMYv5msXl3Y-Ni_0lMpQ");

const sendImageToLLM = async (image) => {
    try {
        const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

        // Define the question
        const question = "Tell what is present in this image. If there is an accident in the image, then only write 'accident'. If there is a woman making a cross sign, then only write 'woman harassment'.";

        // Create a proper prompt
        const prompt = `Context: ${image}\nQuestion: ${question}`;

        // Generate content from the prompt
        const result = await model.generateContent(prompt);

        // Extract and log the response text
        const response = await result.response;
        console.log(response.text());
    } catch (error) {
        console.error("Error communicating with Google Gemini API:", error);
        throw new Error("Failed to generate content from the Google Gemini API.");
    }
};

async function fetchImageAndSend() {
    try {
        // Fetch the image from the URL
        const response = await fetch("http://localhost:8000");

        if (!response.ok) {
            throw new Error(`Failed to fetch image: ${response.statusText}`);
        }

        // Convert response to Blob
        const blob = await response.blob();

        // Convert Blob to Base64
        const base64Image = await convertBlobToBase64(blob);

        // Send the Base64 image to the LLM API
        await sendImageToLLM(base64Image);
    } catch (error) {
        console.error("Error:", error);
    }
}

// Convert Blob to Base64
function convertBlobToBase64(blob) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onloadend = () => resolve(reader.result.split(",")[1]); // Extract Base64 part
        reader.onerror = (error) => reject(error);
    });
}

// Call the function to execute
fetchImageAndSend();
