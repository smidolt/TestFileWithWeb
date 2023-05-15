CREATE TABLE IF NOT EXISTS sreality (
    id SERIAL PRIMARY KEY,      -- Create an id column of type SERIAL (auto-incrementing integer) and make it the primary key
    title TEXT NOT NULL,        -- Create a title column of type TEXT which cannot be NULL
    image_url TEXT NOT NULL     -- Create an image_url column of type TEXT which cannot be NULL
);
